#Python Version 2.7.5
#Author: Aaronn Kelly
#Date begin: 21/04/14

#Crude program that continually reads the serial port the arduino is\
# connected to and prints to terminal.


import serial
from multiprocessing import process
 
ser = serial.Serial(port='/dev/tty.usbmodem621', baudrate=9600)
buffer=[]#buffer of values
headers=["Vin","POut","Preq","PWM"]#column headers

def mainRead( ):
	print("connected to: " + ser.portstr)
	while 1:
		
		if len(buffer)==4: #if the buffer is full then:
			#send values to gui
			#Save to file
			print headers #print the column headers
			print buffer #print the values
			del buffer[:] #Clear the contents of the array
		else:
			val = ser.read()
			buffer.append(val)
		#	print headers
			#print buffer
	
def sendData():
	powerrequired = input('Enter the power required: ')
	ser.write(str(powerrequired).encode())

def parent(): #Master Function call
	while 1:
		thread.start_new(mainRead) #start Serial read
		if raw_input() == 'q': #When Q is pressed, open new thread, which will read input and send to arduino
			thread.start_new(sendData)
		elif raw_input() == 'x': #when x is pressed, end the processs
			break

parent()
