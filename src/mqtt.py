import paho.mqtt.client as mqtt

MQTT_HOST = "18.229.184.215"

BASE_TOPIC = "user/"
BPM_TOPIC = BASE_TOPIC + "heartRate/entry"
RANGE_TOPIC = BASE_TOPIC + "outOfRange/status"
BATTERY_TOPIC = BASE_TOPIC + "battery/level"
EMERGENCY_TOPIC = BASE_TOPIC + "emergency/status"
FALL_DETECTION_TOPIC = BASE_TOPIC + "fall/status"
ARRHYTHMIA_TOPIC = BASE_TOPIC + "arrhythmia/status"

_mqtt = mqtt.Client()

def start():
    _mqtt.on_connect = _on_connect
    _mqtt.connect(MQTT_HOST, 1883, 60)

def notify_emergency(kind):
    _publish(EMERGENCY_TOPIC, kind)

def notify_fall(kind):
    _publish(FALL_DETECTION_TOPIC, kind)

def notify_bpm(bpm):
    _publish(BPM_TOPIC, bpm)

def notify_arrhythmia(kind):
    _publish(FALL_DETECTION_TOPIC, kind)

def notify_battery(value):
    _publish(BATTERY_TOPIC, value)

def notify_range(value):
    _publish(RANGE_TOPIC, value)

def _on_connect():
    print("MQTT connected")

def _publish(topic, data):
    _mqtt.publish(topic, data, retain=True)

