# FACE2MQTT

カメラ画像から顔を検出して、MQTTサーバに情報をpublishする。

## 設計

- 開発言語: python3
- 画像の取得: opencv
- 顔検出: mediapipe
- MQTT通信: paho

## シーケンス

1. IPカメラに接続して、画像を取得
2. MediaPipeを利用して画像中の顔を検出
3. 検出結果 (スコア)をMQTTに通知

## 設定

環境変数を利用して指定

- MQTT_BROKER
- MQTT_PORT
- MQTT_TOPIC
- MQTT_DATA
- IP_CAMERA_URL
- DETECT_LEVEL
- DETECT_INTERVAL

## 実行

```
$ uv sync
$ uv run main.py
```

## デバッグ実行

VSCodeでデバッグ実行

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "main.py",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": "",
            "python": "${workspaceFolder}/.venv/bin/python",
            "console": "integratedTerminal",
            "env": {
                "MQTT_BROKER": "mqtt.local",
                "IP_CAMERA_URL": "http://ipcamera.local:8081"
            },
            "justMyCode": true
        }
    ]
}
```

## サービスとして実行

RaspberryPI OS を想定

### 設定ファイルの配置

face2qtt ファイルを/etc/default/ にコピー。値を修正
face2mqtt.service ファイル中の [Service]セクションのの値を修正
face2mqtt.service ファイルを/etc/systemd/system/ にコピー

### 有効化

```
$ sudo systemctl daemon-reload
$ sudo systemctl enable face2matt
$ sudo systemctl start face2matt
```
