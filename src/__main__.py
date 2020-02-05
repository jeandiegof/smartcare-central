import ble
import mqtt
import time
import notification_handler

def on_disconnection(info):
    notification_handler.on_disconnection()
    print("Restarting BLE")
    ble.run()

def main():
    print("Starting MQTT")
    mqtt.start()

    print("Starting BLE")
    ble.start()

    print("Running BLE")
    device = ble.run()

    print("Registering disconection callback...")
    ble.register_disconnection_callback(device, on_disconnection)

    print("Running...")
    while True:
        time.sleep(1)
        pass

if __name__ == '__main__':
    exit(main())
