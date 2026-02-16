from typing import List
import math
import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

def visualize(img_rgb: np.ndarray, detection_result) -> np.ndarray:
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    # Use the orange color for high visibility.
    cv2.rectangle(img_rgb, start_point, end_point, (0, 165, 255), 3)

    # Draw label and score
    category = detection.categories[0]
    category_name = (category.category_name if category.category_name is not None else '')
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x, MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(img_rgb, result_text, text_location, cv2.FONT_HERSHEY_DUPLEX, FONT_SIZE, TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

  return img_rgb