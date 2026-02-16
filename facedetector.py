import os
import requests
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from typing import List

class FaceDetector:
    def __init__(self):
        self.model_name = 'blaze_face_short_range.tflite'
        if not os.path.isfile(self.model_name):
            self.download_model()
        
        base_options = python.BaseOptions(model_asset_path=self.model_name)
        options = vision.FaceDetectorOptions(base_options=base_options)
        self.detector = vision.FaceDetector.create_from_options(options)

    def download_model(self):
        url = 'https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/' + self.model_name
        urlData = requests.get(url).content
        with open(self.model_name, mode='wb') as f:
            f.write(urlData)

    def detect(self, img_rgb):
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        return self.detector.detect(image)

    def calc_score(self, img_rgb)-> float:
        detection_result = self.detect(img_rgb)
        if len(detection_result.detections) > 0:
            score = detection_result.detections[0].categories[0].score
            return score
        else:
            return 0.0