#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, Response, jsonify
import os
from io import BytesIO
import numpy as np
import cv2
from helpers import getFeatures, drawFeatures
import base64
from PIL import Image
from keras.models import model_from_json
import tensorflow as tf
global graph,model
graph = tf.get_default_graph()

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)
app.config.from_object('config')

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model.h5")

@app.route('/landmarks', methods=['POST', 'GET'])
def home():
    arr = None
    if "image" in request.form:
        img_str = request.form['image']
        img_decoded = base64.b64decode(img_str)
        img_file = Image.open(BytesIO(img_decoded))
        arr = np.asarray(img_file, np.uint8)

    if arr is not None:
        resulter = getFeatures(arr)
        if len(resulter) > 0:
            normalizeddots=[]
            (bbox,dots)=resulter[0]
            (faceX, faceY, faceW, faceH) = bbox
            for (x,y) in dots:
                normalizedX = (x - faceX) / faceW
                normalizedY = (y - faceY) / faceH
                normalizeddots.append(normalizedX)
                normalizeddots.append(normalizedY)
            if len(normalizeddots) == 136:
                img_show = cv2.resize(cv2.cvtColor(arr, cv2.COLOR_RGB2BGR),(int(480),int(640)))

                with graph.as_default():
                    prediction=model.predict(np.array([normalizeddots]))

                flat_list = [int(item*100) for sublist in prediction for item in sublist]
                print(flat_list)

                res = {
                    "category" : flat_list.index(max(flat_list)),
                    "confidence" : max(flat_list)
                }
                return jsonify(category = flat_list.index(max(flat_list)), confidence = max(flat_list))
    else:
        print('err')
        return 'Error'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    