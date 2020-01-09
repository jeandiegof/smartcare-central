#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt

YOUR_DEVICE_ADDRESS = "C4:B2:F1:C9:17:4A"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random

adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(YOUR_DEVICE_ADDRESS, address_type=ADDRESS_TYPE)

for uuid in device.discover_characteristics().keys():
    print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))