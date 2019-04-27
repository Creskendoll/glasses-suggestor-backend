#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, send_file, abort, Response, make_response, Response
import os
from io import BytesIO
import numpy as np
import requests
import cv2
from helpers import getFeature
import base64
from PIL import Image
from json import dumps

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)
app.config.from_object('config')
@app.route('/landmarks', methods=['POST', 'GET'])
def home():
    arr = None
    if "image" in request.form:
        img_str = request.form['image']
        img_decoded = base64.b64decode(img_str)
        img_file = Image.open(BytesIO(img_decoded))
        arr = np.asarray(img_file, np.uint8)

    if arr is not None:
        # cv2.imwrite("img.jpg", 
        #     cv2.cvtColor(arr, cv2.COLOR_RGB2BGR))
        resulter = getFeature(arr)
        # print(resulter)
        return Response(dumps(list(resulter)), mimetype='application/json') 
    else:
        print('err')
        return 'Error'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)