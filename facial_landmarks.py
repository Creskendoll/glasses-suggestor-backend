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

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=False,
	help="path to input image")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

def predictFeature(img):
	result_img = img.copy()
	gray = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)
	# detect faces in the grayscale image
	rects = detector(gray, 1)

	# loop over the face detections
	for (i, rect) in enumerate(rects):
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# convert dlib's rectangle to a OpenCV-style bounding box
		# [i.e., (x, y, w, h)], then draw the face bounding box
		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# show the face number
		cv2.putText(result_img, "Face #{}".format(i + 1), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(result_img, (x, y), 3, (0, 0, 255), -1)
	return result_img

# load the input image, resize it, and convert it to grayscale
if args["image"] is not None:
	image = cv2.imread(args["image"])
	image = imutils.resize(image, width=500)
	featured_img = predictFeature(image)
	# show the output image with the face detections + facial landmarks
	cv2.imshow("Output", featured_img)
	cv2.waitKey(0)
else:
	cam = cv2.VideoCapture(0)
	while True:
		ret, frame = cam.read()
		featured_img = predictFeature(frame)
		cv2.imshow('Res', featured_img)
		# show the output image with the face detections + facial landmarks
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cam.release()
cv2.destroyAllWindows()