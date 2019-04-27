import os
import cv2
import pandas as pd

# from helpers import predictFeature
#read csv
# data =

bbox = (0,0,50,50)

dots = [(0,0),(1,1),(2,0),(0,0),(0,0),(0,0)]

column_names = []for index, dot in enumerate(dots):

   column_names.append('x'+index)

   column_names.append('y'+index)

column_names.append('category')

data = []

for img in os.listdir('./images'):

   row = []

   print('./images/'+img)

   img_file = cv2.imread('./images/'+img,cv2.IMREAD_COLOR)

   rgba_img = cv2.cvtColor(img_file, cv2.COLOR_BGR2RGBA)

   # pred_img = predictFeature(img_file)

   cv2.imshow('win', img_file)

   category = input('Category')

   while category not in range(0,9):

       print('Enter between 1-8')

       category = input('Category')

   row.append(bbox)

   row.append(dots)

   row.append(category)

   data.append(row)

df = pd.DataFrame(data, columns= column_names)
export_csv = df.to_csv(r'C:\\Users\\Admin\\Desktop\\export_dataframe.csv', index = None, header=True)
    


print (df)# save csv to file

cv2.destroyAllWindows()