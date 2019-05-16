import os
import cv2
import pandas as pd
from helpers import getFeatures, drawFeatures

# from helpers import predictFeature
# read csv

bbox = [(0,0,0,0)]
dots= [(0,0)]
column_names = []

for index in range(68):

   column_names.append('x'+str(index))

   column_names.append('y'+str(index))

column_names.append('category')

data = []


for img in os.listdir('./images'):

   row = []

   print('./images/'+img)

   img_file = cv2.imread('./images/'+img,cv2.IMREAD_COLOR)

   rgba_img = cv2.cvtColor(img_file, cv2.COLOR_BGR2RGBA)

   # pred_img = predictFeature(img_file)
   faces = getFeatures(img_file)
   maxDots = 0
   if len(faces) > 0:
      (bbox,dots) = faces[0]
      (faceX, faceY, faceW, faceH) = bbox
      if len(dots) > maxDots:
         maxDots = len(dots)
      cv2.imshow('win', drawFeatures(img_file))

      key = cv2.waitKey(0)
      category = int(chr(key))

      for (x,y) in dots:
         normalizedX = (x - faceX) / faceW
         normalizedY = (y - faceY) / faceH
         row.append(normalizedX)
         row.append(normalizedY)

      if len(dots) < 68:
         for x in range(68 - len(dots)):
            row.append(0)
            row.append(0)

      row.append(category)

      data.append(row)

print(maxDots)

df = pd.DataFrame(data, columns= column_names)
export_csv = df.to_csv(r'./export_dataframe.csv', index = None, header=True)

mass = pd.read_csv(r'./export_dataframe.csv')
print(mass)

# save csv to file

cv2.destroyAllWindows()
