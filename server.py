#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, request, send_file, abort, Response
import os
from helpers import predictFeature

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

@app.route('/landmarks', methods=['POST', 'GET'])
def home():
    return [
        {
            "category" : "A",
            "confidence" : 70
        },
        {
            "category" : "B",
            "confidence" : 25
        },
        {
            "category" : "C",
            "confidence" : 5
        }
    ]

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)