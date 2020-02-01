import ble
import notification_handler
import mqtt

def main():
    print("Starting MQTT")
    mqtt.start()

    print("Starting BLE")
    ble.start()

    print("Trying to connect to", ble.BAND_ADDRESS)
    device = ble.connect(ble.BAND_ADDRESS)

    print("Registering disconection callback...")
    ble.register_disconnection_callback(device, notification_handler.on_disconnection)

    print("Subscribing to characteristics...")
    ble.subscribe_to_button_char(device, notification_handler.on_emergency_notification)
    ble.subscribe_to_bpm_char(device, notification_handler.on_bpm_notification)
    ble.subscribe_to_arrhythmia_char(device, notification_handler.on_arrhythmia_notication)
    ble.subscribe_to_fall_detection_char(device, notification_handler.on_fall_detection_notification)
    ble.subscribe_to_battery_char(device, notification_handler.on_battery_notification)

    print("Running...")
    while True:
        pass

if __name__ == '__main__':
    exit(main())