from imutils import face_utils
import dlib
import cv2
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./training/landmarks.dat")

def getFeatures(img):

	gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
	rects = detector(gray, 1)
	result = []

	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		bbox = face_utils.rect_to_bb(rect)
		result.append((bbox, [dot for dot in shape]))

	return result

def drawFeatures(img):

	result_img = img.copy()
	face_feats = getFeatures(result_img)

	for (bbox, landmarks) in face_feats:
		(x, y, w, h) = bbox
		cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 0, 255), 4)

		for (dot_x, dot_y) in landmarks:
			cv2.circle(result_img, (dot_x, dot_y), 4, (0, 0, 255, 255), -1)

	return result_img
