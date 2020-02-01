import ble
import mqtt
import notification_handler

def on_disconnection(info):
    notification_handler.on_disconnection(1)
    print("Restarting BLE")
    ble.run()

def main():
    print("Starting MQTT")
    mqtt.start()

    print("Starting BLE")
    device = ble.run()

    print("Registering disconection callback...")
    ble.register_disconnection_callback(device, on_disconnection)

    print("Running...")
    while True:
        pass

if __name__ == '__main__':
    exit(main())
