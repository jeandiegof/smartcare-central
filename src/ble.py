#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt

ADDRESS_TYPE = pygatt.BLEAddressType.random
adapter = pygatt.GATTToolBackend()

def start():
	adapter.start()

def scan(print_result=False):
	devices = adapter.scan()
	if print_result == True:
		for device in devices:
			print("###########################")
			print("Name: ", device['name'])
			print("Address", device['address'])
	return devices

def connect(address):
	return adapter.connect(address, address_type=ADDRESS_TYPE)

def discovery_chars(device, print_result=False):
	characteristics = device.discover_characteristics()
	if print_result == True:
		for characteristic in characteristics:
			print(characteristic) 
	return characteristics

def subscribe_to_char(device, char, callback):
	device.subscribe("6e400003-b5a3-f393-e0a9-e50e24dcca9e", callback=callback)

def write_char(device, char, data):
	device.char_write(char, bytearray(data), wait_for_response=True)

def read_char(device, char):
	return device.char_read(char)

def on_disconnection(device, callback):
	device.register_disconnect_callback(callback)
