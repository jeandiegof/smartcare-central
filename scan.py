import bluetooth
import time

def bluetooth_scan():
	SCAN_DURATION = 5
	return bluetooth.discover_devices(duration=SCAN_DURATION, lookup_names = True)

def ble_scan():
	from bluetooth.ble import DiscoveryService
	service = DiscoveryService()
	return service.discover(2)

while True:
	print("Scanning")
	devices = ble_scan()
	if devices:
		for addr, name in devices:
			print(addr, name)
	else:
		print("No devices found")
