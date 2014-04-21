#Python Version 2.7.5
#Author: Aaronn Kelly
#Date begin: 21/04/14


import serial

ser = serial.Serial( #This sets up the serial comms
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

#this will store the line
line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            print("Line: " + line)
            line = []
            break

ser.close()