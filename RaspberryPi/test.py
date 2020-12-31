import bluetooth

target_name = "HC-06"
target_addr = None

for addr in bluetooth.discover_devices():
    if bluetooth.lookup_name( addr ) == target_name:
        target_addr = addr
        break

if target_addr is not None:
    print("found target bluetooth device with address ", target_addr)
else:
    print("could not find target bluetooth device nearby")