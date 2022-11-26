

# if connected change- reload gui with tk.after
# Serial communication baud rate shall be 57600

import serial
import serial.tools.list_ports
import serial.serialutil
import struct
import sys
from storeAttributes import getParams

# Mac ports, for windows you have to find the ports yourself

###
# def cool():
#     frdm_port = "/dev/cu.usbmodem0000001234561"

#     Start = b'\x16'
#     SYNC = b'\x22'
#     Fn_set = b'\x55'
#     red_en = struct.pack("B", 1)  # B stands for 1 byte
#     green_en = struct.pack("B", 0)
#     blue_en = struct.pack("B", 1)
#     off_time = struct.pack("f", 3.1415926)  # float is 4 byte
#     switch_time = struct.pack("H", 500)  # Integer 2 byte

#     Signal_set = Start + Fn_set + red_en + \
#         green_en + blue_en + off_time + switch_time
#     Signal_echo = Start + SYNC + red_en + green_en + blue_en + off_time + switch_time
# #send
#     with serial.Serial(frdm_port, 115200) as pacemaker:
#         pacemaker.write(Signal_set)
# #read
#     with serial.Serial(frdm_port, 115200) as pacemaker:
#         pacemaker.write(Signal_echo)
#         data = pacemaker.read(9)
#         red_rev = data[0]
#         green_rev = data[1]
#         blue_rev = data[2]
#         off_rev = struct.unpack("f", data[3:7])[0]
#         switch_rev = struct.unpack("H", data[7:9])[0]

#     print("From the board:")
#     print("red_en = ", red_rev)
#     print("green_en = ", green_rev)
#     print("blue_en = ", blue_rev)
#     print("off_time = ",  off_rev)
#     print("switch_time = ", switch_rev)
###


def isConnected():
    if sys.platform.startswith('win'):
        try:
            frdm_port = "COM4"
            with serial.Serial(frdm_port, 115200) as pacemaker:
                connected = True
                print("connected")
        except serial.serialutil.SerialException:
            connected = False  # initial value of connected- will change with serial com
            print("not connected")
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        try:
            frdm_port = "/dev/cu.usbmodem0000001234561"
            with serial.Serial(frdm_port, 115200) as pacemaker:
                connected = True
                print("connected")
        except serial.serialutil.SerialException:
            connected = False  # initial value of connected- will change with serial com
            print("not connected")
    return connected, frdm_port


def isDifferent(user):
    comInfo = isConnected()
    findConnection = comInfo[0]
    port = comInfo[1]
    if (findConnection == True):
        print("checking different devices")
        Start = b'\x16'
        SYNC = b'\x22'
        Signal_echo = Start + SYNC
        for i in range(15):
            Signal_echo = Signal_echo+struct.pack("B", 0)
        # comaparing pacemaker data with dcm data
        with serial.Serial(port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            dataIn = pacemaker.read(15)
            currentParams = getParams(user, "checkConn")
            if (struct.unpack("B", dataIn[0:1])[0] != currentParams[4]):  # arp
                return False
            if (dataIn[2] != currentParams[2]):  # apw
                return False
            if (dataIn[3] != currentParams[3]):  # asens
                return False
            if (dataIn[4] != currentParams[1]):  # aamp
                return False
            if (dataIn[5] != currentParams[0]):  # lrl
                return False
            if (dataIn[7] != currentParams[9]):
                return False
            if (struct.unpack("B", dataIn[8:9])[0] != currentParams[10]):
                return False
            if (dataIn[10] != currentParams[5]):
                return False
            if (dataIn[11] != currentParams[6]):
                return False
            if (struct.unpack("B", dataIn[12:13])[0] != currentParams[8]):
                return False
            if (dataIn[14] != currentParams[7]):
                return False
        return True
#         data = pacemaker.read(9)
#         red_rev = data[0]
#         green_rev = data[1]
#         blue_rev = data[2]
#         off_rev = struct.unpack("f", data[3:7])[0]
#         switch_rev = struct.unpack("H", data[7:9])[0]
    else:
        return False


def sendData(paramNative):
    comInfo = isConnected()
    findConnection = comInfo[0]
    port = isConnected[1]
    if (findConnection):
        # send data
        print("sending data")
        Start = b'\x16'
 #     SYNC = b'\x22'
        Fn_set = b'\x55'
        LRLp = struct.pack("f", paramNative[0])
        Aampp = struct.pack("f", paramNative[1])
        apwp = struct.pack("f", paramNative[2])
        Asensp = struct.pack("f", paramNative[3])
        arpp = struct.pack("f", paramNative[4])
        Vampp = struct.pack("f", paramNative[5])
        vpwp = struct.pack("f", paramNative[2])
        Vsensp = struct.pack("f", paramNative[3])
        vrpp = struct.pack("f", paramNative[4])
        Rxp = struct.pack("f", paramNative[9])
        recovp = struct.pack("f", paramNative[10])
        if (paramNative[11] == "AOO"):
            modep = struct.pack("B", 1)
        elif (paramNative[11] == "VVI"):
            modep = struct.pack("B", 4)
        elif (paramNative[11] == "AAI"):
            modep = struct.pack("B", 3)
        elif (paramNative[11] == "VOO"):
            modep = struct.pack("B", 2)
#     switch_time = struct.pack("H", 500)  # Integer 2 byte

        Signal_set = Start + Fn_set + LRLp + Aampp+apwp + \
            Asensp+arpp+Vampp+vpwp+Vsensp+vrpp+Rxp+recovp+modep
        with serial.Serial(port, 115200) as pacemaker:
            pacemaker.write(Signal_set)
    else:
        print("not connected")


def readData():
    comInfo = isConnected()
    findConnection = comInfo[0]
    port = comInfo[1]
    if (findConnection):
        print("checking different devices")
        Start = b'\x16'
        SYNC = b'\x22'
        Signal_echo = Start + SYNC
        for i in range(15):
            Signal_echo = Signal_echo+struct.pack("B", 0)
        # comaparing pacemaker data with dcm data
        with serial.Serial(port, 115200) as pacemaker:
            pacemaker.write(Signal_echo)
            dataIn = pacemaker.read(15)


hi = isDifferent("test")
print(hi)
