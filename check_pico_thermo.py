#!/usr/bin/env python3
import os
import serial
import time
import sys


class Sensor:
    def __init__(self, channel='i', tty='/dev/ttyACM0', speed=9600):
        self.channel=channel
        self.error=None
        try:
            self.sensor=serial.Serial(tty, speed)
        except Exception as e:
            self.error=e

    # Read the pico
    # channel 'd': ds18b20
    #         'i': internal adc thermo
    def __readSerial(self):
        val=0.0
        if self.error==None:
            try:
                self.sensor.write(self.channel) 
                val=self.sensor.readline().strip()
            except Exception as e:
                self.error=e
        return float(val)    


    # Make a statistical cleanup with multiple reads
    def readVal(self):
        vals = [self.__readSerial() for i in range(5)]
        vals.sort()
        return vals[2] #return with the median
        

class Nagios:
    def __init__(self, warning, critical):
        self.warning=warning
        self.critical=critical

    def check(self, val, channel): 
        self.val=val          # Using for the format only
        self.channel=channel  # Using for the format only
        if    val < self.warning:
            self.level, ret = "Normal",   0
        elif  self.warning <= val and val < self.critical: 
            self.level, ret = "Warning",  1
        else: # self.critical <= val
            self.level, ret = "Critical", 2
        
        print("{level} - temperature {channel}:{val} C|ds_themperature={val};{warning};{critical};;".format(**self.__dict__))
        sys.exit(ret)


if __name__ == "__main__":
    if len(sys.argv) > 3:
        channel=sys.argv[1]
        warning=float(sys.argv[2])
        critical=float(sys.argv[3])
    else:
        print("Usage: check_therm_pico.py [i|d] warning-level critical-level")
        sys.exit(2)

    sensor=Sensor(channel)
    nagios=Nagios(warning,critical)
    nagios.check(sensor.readVal(), channel)
