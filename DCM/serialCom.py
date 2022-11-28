

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

def endian_check():
    if sys.byteorder == "little":
        return True
    else:
        return False

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
            dataIn = pacemaker.read(72)
            unpackedDataIn = []
            unpackedDataIn.append(struct.unpack("d", dataIn[0:8])[0]) #lrl
            unpackedDataIn.append(struct.unpack("d", dataIn[8:16])[0]) #url
            unpackedDataIn.append(struct.unpack("d", dataIn[16:24])[0]) #ampl
            unpackedDataIn.append(struct.unpack("d", dataIn[24:32])[0])#pw
            unpackedDataIn.append(struct.unpack("d", dataIn[32:40])[0])#atr_sen
            unpackedDataIn.append(struct.unpack("d", dataIn[40:48])[0])#vent_sen
            unpackedDataIn.append(struct.unpack("d", dataIn[48:56])[0])#atr_ref
            unpackedDataIn.append(struct.unpack("d", dataIn[56:64])[0])#vent_ref
            unpackedDataIn.append(struct.unpack("d", dataIn[64:72])[0])#mode
            currentParams = getParams(user, "checkConn")
            #print(unpackedDataIn)
            if (currentParams == None or dataIn == None):
                return True
            if (unpackedDataIn[2] == currentParams[2] or unpackedDataIn[2] == currentParams[6]):  # amp
                pass
            else:
                return True
            if (unpackedDataIn[3] == currentParams[3] or unpackedDataIn[3] == currentParams[7]):  # pw
                pass
            else:
                return True
            if (unpackedDataIn[6] != currentParams[5]):  # arp
                return True
            if (unpackedDataIn[7] != currentParams[7]):  # vrp
                return True
            if (unpackedDataIn[0] != currentParams[0]):  # lrl
                return True
            if (unpackedDataIn[1] != currentParams[1]):  # URL
                return True
            if (dataIn[4] != currentParams[4]):  # Asens
                return True
            if (unpackedDataIn[5] != currentParams[8]):  # Vsens
                return True
        return False
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
    port = comInfo[1]
    if (findConnection):
        # send data
        print("sending data")
        Start = b'\x16'
        SYNC = b'\x22'
        Fn_set = b'\x55'
        print(paramNative)
        if (paramNative[11] == "AOO"):
            if(endian_check()==True):
                print('little endian')
                Aampp = struct.pack("<d", paramNative[1])
                apwp = struct.pack("<d", paramNative[2])
                arpp = struct.pack("<d", paramNative[4])
                vrpp = struct.pack("<d", paramNative[4])
                LRLp = struct.pack("<d", paramNative[0])
                URLp = struct.pack("<d", paramNative[12])
                Asensp = struct.pack("<d", paramNative[3])
                Vsensp = struct.pack("<d", paramNative[3])
                modep = struct.pack("d", 1)
            else:
                print('big endian')
                Aampp = struct.pack(">d", float(paramNative[1]))
                apwp = struct.pack(">d", float(paramNative[2]))
                arpp = struct.pack(">d", float(paramNative[4]))
                vrpp = struct.pack(">d", float(paramNative[4]))
                LRLp = struct.pack(">d", float(paramNative[0]))
                URLp = struct.pack(">d", float(paramNative[12]))
                Asensp = struct.pack(">d", float(paramNative[3]))
                Vsensp = struct.pack(">d", float(paramNative[3]))
                modep = struct.pack("d", 1)
            Signal_set = Start + Fn_set + Aampp+apwp + \
                arpp+vrpp+LRLp+URLp+Asensp+Vsensp+modep
        elif (paramNative[11] == "VVI"):
            if(endian_check()==True):
                Vampp = struct.pack("<d", paramNative[5])
                vpwp = struct.pack("<d", paramNative[6])
                arpp = struct.pack("<d", paramNative[4])
                vrpp = struct.pack("<d", paramNative[4])
                LRLp = struct.pack("<d", paramNative[0])
                URLp = struct.pack("<d", paramNative[12])
                Asensp = struct.pack("<d", paramNative[3])
                Vsensp = struct.pack("<d", paramNative[3])
                modep = struct.pack("d", 4)
            else:
                Vampp = struct.pack(">d", paramNative[5])
                vpwp = struct.pack(">d", paramNative[6])
                arpp = struct.pack(">d", paramNative[4])
                vrpp = struct.pack(">d", paramNative[4])
                LRLp = struct.pack(">d", paramNative[0])
                URLp = struct.pack(">d", paramNative[12])
                Asensp = struct.pack(">d", paramNative[3])
                Vsensp = struct.pack(">d", paramNative[3])
                modep = struct.pack("d", 4)
            Signal_set = Start + Fn_set + Vampp+vpwp + \
                arpp+vrpp+LRLp+URLp+Asensp+Vsensp+modep
        elif (paramNative[11] == "AAI"):
            Aampp = struct.pack("f", paramNative[1])
            apwp = struct.pack("f", paramNative[2])
            arpp = struct.pack("f", paramNative[4])
            vrpp = struct.pack("f", paramNative[4])
            LRLp = struct.pack("f", paramNative[0])
            URLp = struct.pack("f", paramNative[12])
            Asensp = struct.pack("f", paramNative[3])
            Vsensp = struct.pack("f", paramNative[3])
            modep = struct.pack("f", 3)
            Signal_set = Start + Fn_set + Aampp+apwp + \
                arpp+vrpp+LRLp+URLp+Asensp+Vsensp+modep
        elif (paramNative[11] == "VOO"):
            if(endian_check()==True):
                print('little endian')
                Vampp = struct.pack("<d", paramNative[5])
                vpwp = struct.pack("<d", paramNative[6])
                arpp = struct.pack("<d", paramNative[4])
                vrpp = struct.pack("<d", paramNative[4])
                LRLp = struct.pack("<d", paramNative[0])
                URLp = struct.pack("<d", paramNative[12])
                Asensp = struct.pack("<d", paramNative[3])
                Vsensp = struct.pack("<d", paramNative[3])
                modep = struct.pack("d", 2)
            else:
                print('big endian')
                Vampp = struct.pack(">d", paramNative[5])
                vpwp = struct.pack(">d", paramNative[6])
                arpp = struct.pack(">d", paramNative[4])
                vrpp = struct.pack(">d", paramNative[4])
                LRLp = struct.pack(">d", paramNative[0])
                URLp = struct.pack(">d", paramNative[12])
                Asensp = struct.pack(">d", paramNative[3])
                Vsensp = struct.pack(">d", paramNative[3])
                modep = struct.pack("d", 2)
            Signal_set = Start + Fn_set + Vampp+vpwp + \
                arpp+vrpp+LRLp+URLp+Asensp+Vsensp+modep
#     switch_time = struct.pack("H", 500)  # Integer 2 byte
        with serial.Serial(port, 115200) as pacemaker:
            pacemaker.write(Signal_set)
    else:
        print("not connected")
        # print(paramNative)
    #print(Signal_set)

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
            return dataIn
    else:
        return None


def testSet():
    comInfo = isConnected()
    findConnection = comInfo[0]
    port = comInfo[1]
    if (findConnection):
        # send data
        print("sending data")
        Start = b'\x16'
 #     SYNC = b'\x22'
        Fn_set = b'\x55'
        LRLp = struct.pack("f", 35)
        Aampp = struct.pack("f", 1)
        apwp = struct.pack("f", 3)
        Asensp = struct.pack("f", 3)
        arpp = struct.pack("f", 3)
        Vampp = struct.pack("f", 0)
        vpwp = struct.pack("f", 0)
        Vsensp = struct.pack("f", 0)
        vrpp = struct.pack("f", 0)
        Rxp = struct.pack("f", 0)
        recovp = struct.pack("f", 0)
        modep = struct.pack("B", 1)
#     switch_time = struct.pack("H", 500)  # Integer 2 byte
        Signal_set = Start + Fn_set + LRLp + Aampp+apwp + \
            Asensp+arpp+Vampp+vpwp+Vsensp+vrpp+Rxp+recovp+modep
        with serial.Serial(port, 115200) as pacemaker:
            pacemaker.write(Signal_set)

    else:
        print("not connected")
        # print(paramNative)


def setRx():
    print("checking different devices")
    Start = b'\x16'
    SYNC = b'\x22'
    Signal_echo = Start + SYNC
    for i in range(15):
        Signal_echo = Signal_echo+struct.pack("B", 0)
    # comaparing pacemaker data with dcm data
    with serial.Serial("Com4", 115200) as pacemaker:
        pacemaker.write(Signal_echo)
        dataIn = pacemaker.read(15)
        print(dataIn)


# testSet()

# setRx() uncoment to test gui recieve
