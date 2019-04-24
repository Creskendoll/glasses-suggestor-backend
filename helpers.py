from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("landmarks.dat")

def predictFeature(img):

	result_img = img.copy()
	gray = cv2.cvtColor(result_img, cv2.COLOR_RGBA2GRAY)
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
		cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 0, 255), 2)

		# show the face number
		cv2.putText(result_img, "Face #{}".format(i + 1), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0, 255), 2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(result_img, (x, y), 3, (0, 0, 255, 255), -1)
	return result_img
