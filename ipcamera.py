import requests
import cv2
import numpy as np

class IPCamera:
    def __init__(self, url, rotate=0, flip=0):
        self.url = url
        self.rotate = rotate
        self.flip = flip

    def take_snapshot(self):
        response = requests.get(self.url)
        image_array = np.frombuffer(response.content, dtype=np.uint8)
        img_bgr = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        
        if self.rotate == 1:
            img_rgb = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
        elif self.rotate == 2:
            img_rgb = cv2.rotate(img_rgb, cv2.ROTATE_180_CLOCKWISE)
        elif self.rotate == 3:
            img_rgb = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        if self.flip == 1:
            img_rgb = cv2.flip(img_rgb, 0)
        elif self.flip == 2:
            img_rgb = cv2.flip(img_rgb, 1)
        elif self.flip == 3:
            img_rgb = cv2.flip(img_rgb, -1)

        return img_rgb

