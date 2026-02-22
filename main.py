import os
import time
from datetime import datetime
import platform
import random
from paho.mqtt import client as mqtt_client
from ipcamera import IPCamera
from facedetector import FaceDetector

MQTT_BROKER      = os.getenv('MQTT_BROKER',      'mqtt.local')
MQTT_PORT        = os.getenv('MQTT_PORT',        '1883')
MQTT_TOPIC       = os.getenv('MQTT_TOPIC',       'face2mqtt')
MQTT_DATA        = os.getenv('MQTT_DATA',        '{\"type\":\"start\"}')
IP_CAMERA_URL    = os.getenv('IP_CAMERA_URL',    'http://ipcamera.local:8081')
IP_CAMERA_ROTATE = os.getenv('IP_CAMERA_ROTATE', '0')
IP_CAMERA_FLIP   = os.getenv('IP_CAMERA_FLIP',   '0')
DETECT_LEVEL     = os.getenv('DETECT_LEVEL',     '0.7')
DETECT_INTERVAL  = os.getenv('DETECT_LEVEL',     '1.0')

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("MQTT connected.")
    else:
        print(f"MQTT connect failed! reason_code: {reason_code}")

def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    if reason_code == 0:
        print("MQTT disconnected.")
    else:
        print(f"MQTT disconnection failed! reason_code: {reason_code}")

client_id = 'FaceDatection-' + platform.node() + '-' + str(random.randint(0, 1000))
client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect(MQTT_BROKER, int(MQTT_PORT))
client.loop_start()

camera = IPCamera(IP_CAMERA_URL, IP_CAMERA_ROTATE, IP_CAMERA_FLIP)
detector = FaceDetector()

while(True):
    img_rgb = camera.take_snapshot()
    score = detector.calc_score(img_rgb)
    print('Face detected! score=' + str(score))
    if score > float(DETECT_LEVEL):    
        client.publish(MQTT_TOPIC, MQTT_DATA)
    time.sleep(float(DETECT_INTERVAL))
