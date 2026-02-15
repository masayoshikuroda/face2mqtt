import requests
import cv2
import numpy as np

class IPCamera:
    def __init__(self, url):
        self.url = url

    def take_snapshot(self):
        response = requests.get(self.url)
        image_array = np.frombuffer(response.content, dtype=np.uint8)
        img_bgr = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        return img_rgb

