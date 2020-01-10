#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt

def on_disconnection(handle):
	print("Device disconnected")

def on_data(handle, value):
	print("Data received: ", value);

DEVICE_ADDRESS = "C4:B2:F1:C9:17:4A"
ADDRESS_TYPE = pygatt.BLEAddressType.random

adapter = pygatt.GATTToolBackend()
adapter.start()

print("Connecting to device ", DEVICE_ADDRESS)
device = adapter.connect(DEVICE_ADDRESS, address_type=ADDRESS_TYPE)
device.register_disconnect_callback(on_disconnection)
print("Subscribing")
device.subscribe("6e400003-b5a3-f393-e0a9-e50e24dcca9e", callback=on_data)
print("Done");
device.char_write("6e400002-b5a3-f393-e0a9-e50e24dcca9e", bytearray([48, 49]), wait_for_response=True)

def main():
	for uuid in device.discover_characteristics().keys():
		print("Read UUID", uuid)
#		print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))

	while True:
		pass

if __name__ == '__main__':
	exit(main())

