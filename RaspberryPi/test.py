import serial

port = "/dev/rfcomm0"
serial = serial.Serial(port,9600)

while(True):
    line = serial.readline()
    if not line: continue
    print(line)
    serial.write(line)
    serial.flushInput()