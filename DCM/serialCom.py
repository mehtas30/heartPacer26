import serial

# ser = serial.Serial('COM5', 115200, timeout=10)

connected = False  # initial value of connected- will change with serial com
pmID = 341  # example pace maker ID from serial com- will store to db for next time
previousId = 431  # will get from database
if (pmID == previousId):  # checks id of pacemaker and gives value to boolean different
    different = False
else:
    different = True

# if connected change- reload gui with tk.after
#Serial communication baud rate shall be 57600

import serial
import serial.tools.list_ports
import struct

# Mac ports, for windows you have to find the ports yourself
frdm_port = "/dev/cu.usbmodem0000001234561"

Start = b'\x16'
SYNC = b'\x22'
Fn_set = b'\x55'
red_en = struct.pack("B", 1)
green_en = struct.pack("B", 0)
blue_en = struct.pack("B", 1)
off_time = struct.pack("f", 3.1415926)
switch_time = struct.pack("H", 500)

Signal_set = Start + Fn_set + red_en + green_en + blue_en + off_time + switch_time
Signal_echo = Start + SYNC + red_en + green_en + blue_en + off_time + switch_time

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_set)

with serial.Serial(frdm_port, 115200) as pacemaker:
    pacemaker.write(Signal_echo)
    data = pacemaker.read(9)
    red_rev = data[0]
    green_rev = data[1]
    blue_rev = data[2]
    off_rev =  struct.unpack("f", data[3:7])[0]
    switch_rev =  struct.unpack("H", data[7:9])[0]

print("From the board:")
print("red_en = ", red_rev)
print("green_en = ", green_rev)
print("blue_en = ", blue_rev)
print("off_time = ",  off_rev)
print("switch_time = ", switch_rev)