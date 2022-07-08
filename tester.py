#!/usr/bin/env python3
import os
import serial

try:
    sensor=serial.Serial('/dev/ttyACM0', 115200)
    print("sensor opened")
except:
    pass


try:
    sensor.write('i') 
    internal=sensor.readline().strip() 
except:
    internal="NaN"

print("internal", internal)

try:
    sensor.write('d') 
    ds=sensor.readline().strip() 
except:
    ds="NaN"

print("dallas", ds)

try: 
    sensor.close()
except:
    pass

print("internal: {0} ds: {1}".format( internal, ds))


