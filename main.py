'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import cv2
from functools import partial
import numpy as np
from helpers import predictFeature

# Builder.load_string('''
# <MyCamera>:
#     orientation: 'vertical'
#     Camera:
#         id: camera
#         resolution: (640, 480)
#         play: True

#     Button:
#         text: 'Capture'
#         size_hint_y: None
#         height: '48dp'
#         on_press: root.capture()
# ''')

class MyCamera(Camera):

    def on_tex(self, *l):
        texture = self.texture
        arr = np.reshape(np.fromstring(texture.pixels, dtype=np.uint8), 
            (self.texture_size[1], self.texture_size[0], 4))
        predArr = predictFeature(arr)

        self.texture.blit_buffer(predArr.tostring(), bufferfmt="ubyte", colorfmt="rgba")

        return super().on_tex(*l)


class MyApp(App):

    def build(self):
        view = BoxLayout()
        view.orientation = "vertical"

        cam = MyCamera(resolution=(640, 480), play=True)

        btn = Button(text="Capture")
        btn.size_hint_y = None
        btn.height = '48dp'
        btn.bind(on_press=partial(self.capture, cam))

        view.add_widget(btn)
        view.add_widget(cam)
        return view
    
    def capture(self, camera, value):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        texture = camera.texture

        arr = np.fromstring(texture.pixels, dtype=np.uint8)
        a = np.reshape(arr, (camera.texture_size[1], camera.texture_size[0], 4))
        a = cv2.cvtColor(a, cv2.COLOR_RGBA2BGR)

        cv2.imshow("frame", a)

if __name__ == "__main__":
    MyApp().run()
