#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt
import notification_handler

ADDRESS_TYPE = pygatt.BLEAddressType.random
adapter = pygatt.GATTToolBackend()

BAND_ADDRESS = "EB:94:D6:DB:4F:B4"

BUTTON_CHARACTERISTIC = "45ce1501-392c-4d5a-b520-54667cb00609"
BPM_CHARACTERISTIC = "45ce1502-392c-4d5a-b520-54667cb00609"
ARRHYTHMIA_CHARACTERISTIC = "45ce1503-392c-4d5a-b520-54667cb00609"
FALL_DETECTION_CHARACTERISTIC = "45ce1504-392c-4d5a-b520-54667cb00609"
BATTERY_CHARACTERISTIC = "45ce1505-392c-4d5a-b520-54667cb00609"

def run():
    print("Trying to connect to", BAND_ADDRESS)
    device = connect(BAND_ADDRESS)
    notification_handler.on_connection()

    print("Subscribing to characteristics...")
    subscribe_to_button_char(device, notification_handler.on_emergency_notification)
    subscribe_to_bpm_char(device, notification_handler.on_bpm_notification)
    subscribe_to_arrhythmia_char(device, notification_handler.on_arrhythmia_notication)
    subscribe_to_fall_detection_char(device, notification_handler.on_fall_detection_notification)
    subscribe_to_battery_char(device, notification_handler.on_battery_notification)

    return device

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
    while True:
        try:
            device = adapter.connect(address, address_type=ADDRESS_TYPE)
            return device
        except:
            print("Failed to connect to", BAND_ADDRESS)

def discovery_chars(device, print_result=False):
    characteristics = device.discover_characteristics()
    if print_result == True:
        for characteristic in characteristics:
            print(characteristic) 
    return characteristics

def subscribe_to_char(device, char, callback):
    device.subscribe(char, callback=callback)

def write_char(device, char, data):
    device.char_write(char, bytearray(data), wait_for_response=True)

def read_char(device, char):
    return device.char_read(char)

def register_disconnection_callback(device, callback):
    device.register_disconnect_callback(callback)

def subscribe_to_button_char(device, callback):
    device.subscribe(BUTTON_CHARACTERISTIC, callback=callback)

def subscribe_to_bpm_char(device, callback):
    device.subscribe(BPM_CHARACTERISTIC, callback=callback)

def subscribe_to_arrhythmia_char(device, callback):
    device.subscribe(ARRHYTHMIA_CHARACTERISTIC, callback=callback)

def subscribe_to_fall_detection_char(device, callback):
    device.subscribe(FALL_DETECTION_CHARACTERISTIC, callback=callback)

def subscribe_to_battery_char(device, callback):
    device.subscribe(BATTERY_CHARACTERISTIC, callback=callback)
