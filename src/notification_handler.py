import mqtt


def on_emergency_notification(handle, value):
    print("On emergency", to_string(value))
    mqtt.notify_emergency(to_string(value))


def on_bpm_notification(handle, value):
    print("On bpm", to_string(value))
    mqtt.notify_bpm(to_string(value))


def on_arrhythmia_notication(handle, value):
    print("On arrhythmia", to_string(value))
    mqtt.notify_arrhythmia(to_string(value))


def on_fall_detection_notification(handle, value):
    print("On fall detection", to_string(value))
    mqtt.notify_fall(to_string(value))


def on_battery_notification(handle, value):
    print("On battery", to_string(value))
    mqtt.notify_battery(to_string(value))


def on_connection():
    mqtt.notify_range(0)


def on_disconnection():
    mqtt.notify_range(1)


def to_string(value):
    return "".join(list(map(str, value)))
