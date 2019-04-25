'''
Camera
======

Note that not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import cv2
from functools import partial
import numpy as np
from helpers import predictFeature

class MyCamera(Camera):

    # Called on each frame
    def on_tex(self, *l):
        '''
        Function which gets called on each camera frame
        '''

        arr = np.reshape(np.fromstring(self.texture.pixels, dtype=np.uint8), 
            (self.texture_size[1], self.texture_size[0], 4))

        predArr = predictFeature(arr)

        self.texture.blit_buffer(predArr.tostring(), bufferfmt="ubyte", colorfmt="rgba")

        return super().on_tex(*l)


class MyApp(App):

    # Called once
    def build(self):
        # Root layout
        view = BoxLayout()
        view.orientation = "vertical"

        # Camera instance
        cam = MyCamera(resolution=(480, 1280), play=True)

        # Button
        btn = Button(text="Capture")
        btn.size_hint_y = None
        btn.height = '48dp'
        btn.bind(on_press=partial(self.capture, cam))

        # Add components to view
        view.add_widget(btn)
        view.add_widget(cam)
        return view
    
    def capture(self, camera, value):
        '''
        Function which gets called when the button is pressed
        '''
        # Camera texture
        texture = camera.texture

        # Convert texture to np array
        img = np.reshape(np.fromstring(texture.pixels, dtype=np.uint8),
            (camera.texture_size[1], camera.texture_size[0], 4))
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        # Show img
        cv2.imshow("Image", img)

if __name__ == "__main__":
    MyApp().run()
