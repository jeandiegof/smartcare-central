import mqtt_config
import requests
import json

PARSE_HEADERS = {
    "X-Parse-Application-Id": "ap-id-rergs",
    "Content-Type": "application/json",
}
PARSE_BASE_URL = "http://18.229.184.215:1337/parse/classes/"
PARSE_HEART_RATE_CLASS = "HeartRateEntry"
PARSE_FALL_DETECTION_CLASS = "Fall"
PARSE_OUT_OF_RANGE_CLASS = "OutOfRange"
PARSE_EMERGENCY_CLASS = "Emergency"


def dispatch(topic, payload):
    print("dispatching message!!!")
    print("topic: ", topic)
    if topic == mqtt_config.HEART_RATE_TOPIC:
        print("heart rate:", payload)
        post_heart_rate(payload)
    elif topic == mqtt_config.OUT_OF_RANGE_TOPIC:
        print("out of range")
        post_out_of_range(payload)
    elif topic == mqtt_config.EMERGENCY_TOPIC:
        print("emergency")
        post_emergency(payload)
    elif topic == mqtt_config.FALL_DETECTION_TOPIC:
        print("fall detection")
        post_fall_detection(payload)
    else:
        print("no match")
    print("finalize")


def post_heart_rate(value):
    data = '{"value": ' + value.decode("ASCII") + " }"
    print(_post(PARSE_HEART_RATE_CLASS, data))


def post_out_of_range(status):
    payload = "true" if status.decode("ASCII") == "1" else "false"
    data = '{"outOfRangeStatus": ' + payload + " }"
    print(_post(PARSE_OUT_OF_RANGE_CLASS, data))


def post_emergency(status):
    payload = (
        "true"
        if status.decode("ASCII") == "1" or status.decode("ASCII") == "2"
        else "false"
    )
    data = '{"emergencyStatus": ' + payload + " }"
    print(data)
    print(_post(PARSE_EMERGENCY_CLASS, data))


def post_fall_detection(status):
    payload = "true" if status.decode("ASCII") == "1" else "false"
    data = '{"fallStatus": ' + payload + " }"
    print(data)
    print(_post(PARSE_FALL_DETECTION_CLASS, data))


def _post(parse_class, data):
    return requests.post(
        PARSE_BASE_URL + parse_class, headers=PARSE_HEADERS, data=data,
    )
