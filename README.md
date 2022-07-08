# Pico thermometer integrated to nagios 


## Build

```bash
git submodule update --init
mkdir build
cd build
cmake ..
make
```

## Setup

 1. push and keep the reset button on the raspberry pi pico
 2. connect the device to the PC
 3. wait for the beep
 4. release the button
 5. copy the .uf2 to the device.

 <img src="https://raw.github.com/jsheperd/pico_nagios_thermo/main/img/hardware.jpg" width="200" height="200" />

## Use it

 1. ls /dev/ttyACM*
 2. Connect the USB
 3. ls /dev/ttyACM* will show the new device on the list
 4. cat the device from a terminal 
 ```bash
 sudo cat /dev/ttyACM0
 ```
 5. in another terminal echo an 'i' to get the internal sensor value
 ```bash
 sudo su
 echo i > /dev/ttyACM0
 ```
 6. You can see the return value on the first terminal
 7. tester.py shows how to use from python

 <img src="https://raw.github.com/jsheperd/pico_nagios_thermo/main/img/read_bash.png" width="200" height="200" />

## Nagios

As nagios checks run under the nagios user, we should make the sensor readable for nagios.

```bash
chown nagios:nagios /dev/ttyACM0
```

We can make it permanent after reconnect.

```bash
cp 60-extra-acl.rules /etc/udev/rules.d
```



