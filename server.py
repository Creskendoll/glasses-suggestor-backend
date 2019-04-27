#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, send_file, abort, Response
import os
from io import BytesIO
import numpy as np
import requests
import cv2
from helpers import getFeature
import base64

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)
app.config.from_object('config')
@app.route('/landmarks', methods=['POST', 'GET'])
def home():
    
    arr = None
    json_data = request.get_json() 
    if "image" in json_data:
        img_str = json_data['image']
        encoded = base64.b64encode(img_str.encode())
        decoded = base64.decodebytes(encoded)
        arr = np.frombuffer(decoded, np.uint8)
        arr = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if arr is not None:
        print(arr)
        resulter = getFeature(arr)
        print(resulter)
        return str(resulter) 
    else: 
        print('err')
        return 'Error'
    # return '
    #         "category" : "A",
    #        "confidence" : 70
       
       
    #         "category" : "B",
    #         "confidence" : 25
        
        
    #         "category" : "C",
    #         "confidence" : 5
    #      '
    # return [
    #     {
    #         "category" : "A",
    #         "confidence" : 70
    #     },
    #     {
    #         "category" : "B",
    #         "confidence" : 25
    #     },
    #     {
    #         "category" : "C",
    #         "confidence" : 5
    #     }
    # ]
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)