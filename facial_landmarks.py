# import the necessary packages
import cv2
from helpers import drawFeatures

cam = cv2.VideoCapture(0)
while True:
	ret, frame = cam.read()
	featured_img = drawFeatures(frame)
	cv2.imshow('Res', featured_img)
	# show the output image with the face detections + facial landmarks
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()