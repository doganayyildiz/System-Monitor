import struct

import serial, time
import psutil

ser = serial.Serial('/dev/cu.usbmodem14101',115200)

while True:
    cpu = str(int(psutil.cpu_percent()))
    ram = str(int(psutil.virtual_memory().percent))
    ser.write(cpu.encode())
    ser.write(b'\n')
    ser.write(ram.encode())
    ser.write(b'\n')
    print("CPU: ",cpu,"--------","RAM: ",ram)


    time.sleep(1)