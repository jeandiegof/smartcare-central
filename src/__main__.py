import ble

BAND_ADDRESS = "C4:B2:F1:C9:17:4A"

def on_disconnection(handle):
	print("Device disconnected")

def on_data(handle, value):
	print("Data received: ", value)

def main():
    print("Starting BLE")
    ble.start()

    print("Trying to connect to ", BAND_ADDRESS)
    device = ble.connect(BAND_ADDRESS)

    print("Registering disconection callback")
    ble.on_disconnection(device, on_disconnection)

    print("Discovering characteristcs")
    ble.discovery_chars(device, print_result=True)

    print("Subscribing")
    ble.subscribe_to_char(device, "6e400003-b5a3-f393-e0a9-e50e24dcca9e", callback=on_data)

    print("Writing into characteristc")
    ble.write_char(device, "6e400002-b5a3-f393-e0a9-e50e24dcca9e", [48, 49])

    print("Running...")
    while True:
        pass

if __name__ == '__main__':
    exit(main())