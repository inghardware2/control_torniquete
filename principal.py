import I2C_LCD_driver
from datetime import datetime

import RPi.GPIO as GPIO

import time
import sys

buzzer = 17
relayIN = 27
relayOUT = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)

GPIO.setup(relayIN,GPIO.OUT)
GPIO.output(relayIN,GPIO.LOW)

GPIO.setup(relayOUT,GPIO.OUT)
GPIO.output(relayOUT,GPIO.LOW)

lcd = I2C_LCD_driver.lcd()

customC = [
        #error
        [ 0b00000,
          0b11011,
          0b01110,
          0b00100,
          0b01110,
          0b11011,
          0b00000,
          0b00000 ],
        #chulito
        [ 0b00000,
          0b00001,
          0b00011,
          0b10110,
          0b11100,
          0b01000,
          0b00000,
          0b00000 ],
]

def iconStatusInternet(i):
    lcd.lcd_display_string("I",1,15)
    if i == 0: #indicador false
        lcd.lcd_load_custom_chars(customC)
        lcd.lcd_write(144)
        lcd.lcd_write_char(0)
    elif i == 1: #indicador true
        lcd.lcd_load_custom_chars(customC)
        lcd.lcd_write(144)
        lcd.lcd_write_char(1)

def iconStatusServer(i):
    lcd.lcd_display_string("S",1,18)
    if i == 0: #indicador false
        lcd.lcd_load_custom_chars(customC)
        lcd.lcd_write(147)
        lcd.lcd_write_char(0)
    elif i == 1: #indicador true
        lcd.lcd_load_custom_chars(customC)
        lcd.lcd_write(147)
        lcd.lcd_write_char(1)

if int(sys.argv[1]) == 0:
    #lcd.lcd_clear() 
	lcd.lcd_display_string("DENEGADO",3,6)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(buzzer,GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(buzzer,GPIO.LOW)
	time.sleep(0.1)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(buzzer,GPIO.LOW)
	time.sleep(0.2)
          
if int(sys.argv[1]) == 1:
        #lcd.lcd_clear()
        lcd.lcd_display_string("BIENVENIDO",2,5)
        timeString = datetime.now().strftime('%H:%M:%S')
        lcd.lcd_display_string(timeString,3,6)
        GPIO.output(relayIN,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayIN,GPIO.LOW)     

        
time.sleep(1)

lcd.lcd_clear()
dateString = datetime.now().strftime('%d/%m/%y')
lcd.lcd_display_string(dateString, 1,0)
lcd.lcd_display_string("COLOQUE SU HUELLA",3,1)

if int(sys.argv[2]) == 0:
	iconStatusInternet(0)  
elif int(sys.argv[2]) == 1:
	iconStatusInternet(1)   

if int(sys.argv[3]) == 0:
	iconStatusServer(0)  
elif int(sys.argv[3]) == 1:
	iconStatusServer(1)   
	
#iconStatusInternet(1)
#iconStatusServer(1)

#time.sleep(1)


