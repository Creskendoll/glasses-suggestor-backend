import os
import cv2
from helpers import predictFeature
import tkinter as tk

TRAIN_IMAGES = "./training/"

gui_root = tk.Tk()

canvas = tk.Canvas(gui_root, width = 500, height = 500)
canvas.pack()
img = tk.PhotoImage()
btn = tk.Button(gui_root, text="Button")
btn.pack(side="left")

canvas.create_image(20,20,anchor=tk.NW,image=img)


for img_file in os.listdir(TRAIN_IMAGES):
    img.file = img_file
    img = cv2.waitKey(0)
    # pred_img = predictFeature(img)
    # cv2.imshow("Landmarks", pred_img)

gui_root.mainloop()