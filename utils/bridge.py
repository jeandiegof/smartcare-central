import paho.mqtt.client as mqtt
import dispatcher
import mqtt_config

_mqtt = mqtt.Client()


def main():
    _mqtt.on_connect = _on_connect
    _mqtt.on_message = _on_message
    _mqtt.connect(mqtt_config.MQTT_HOST, 1883, 60)
    _subscribe()
    _mqtt.loop_forever()


def _on_connect():
    _subscribe()


def _on_message(client, userdata, message):
    print("MQTT message")
    print("Topic", message.topic)
    print("Payload", message.payload)
    dispatcher.dispatch(message.topic, message.payload)


def _subscribe():
    _mqtt.subscribe(mqtt_config.HEART_RATE_TOPIC)
    _mqtt.subscribe(mqtt_config.OUT_OF_RANGE_TOPIC)
    _mqtt.subscribe(mqtt_config.EMERGENCY_TOPIC)
    _mqtt.subscribe(mqtt_config.FALL_DETECTION_TOPIC)


if __name__ == "__main__":
    exit(main())
