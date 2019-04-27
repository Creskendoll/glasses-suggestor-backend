# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg
#

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from helpers import predictFeature, getFeature

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
# 	help="path to facial landmark predictor")
# ap.add_argument("-i", "--image", required=False,
# 	help="path to input image")
# args = vars(ap.parse_args())

# load the input image, resize it, and1 convert it to grayscale
# if args["image"] is not None:
# 	image = cv2.imread(args["image"])
# 	image = imutils.resize(image, width=500)
# 	featured_img = predictFeature(image)
# 	# show the output image with the face detections + facial landmarks
# 	cv2.imshow("Output", featured_img)
# 	cv2.waitKey(0)
# else:


cam = cv2.VideoCapture(0)
while True:
	ret, frame = cam.read()
	featured_img = predictFeature(frame)
	cv2.imshow('Res', featured_img)
	resulter = getFeature(frame)
	print(resulter)
	# show the output image with the face detections + facial landmarks
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()