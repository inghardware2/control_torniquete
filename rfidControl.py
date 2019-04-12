import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

portS = serial.Serial('/dev/ttySAC0',9600)

while True:
     ID = ""
     tag = portS.read()  
     if tag=="\x02":
         for Counter in range(12):
 		    tag=portS.read()
		    if (Counter > 9):
			   i= int(ID,16)
			   print i
		    elif (Counter >3):
			    ID = ID + str(tag)	 
