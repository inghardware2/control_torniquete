import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


portS = serial.Serial('/dev/ttySAC0',9600)

tag = str('150007F7AE4B')

while True:
     ID = ""
     read_byte = portS.read()
  
     if read_byte=="\x02":
         for Counter in range(12):
 		    read_byte=portS.read()
		    ID = ID + str(read_byte)
	 if ID == tag:
		print "Access true"
         
