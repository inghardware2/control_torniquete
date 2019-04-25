import I2C_LCD_driver
import statusIndicator
from datetime import datetime
from subprocess import call
import RPi.GPIO as GPIO
import time
import sys

#pin configuration
buzzer = 22

#port configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initial states
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)

#object statement
lcd = I2C_LCD_driver.lcd()

lcd.lcd_clear() 
lcd.lcd_display_string("SISTEMA",2,7)
lcd.lcd_display_string("BLOQUEADO",3,6)

GPIO.output(buzzer,GPIO.HIGH)

call('halt -p', shell=True)

#active buzzer
# def buzzer_alert():
	# #for x in range(3):
	# GPIO.output(buzzer,GPIO.HIGH)
	# time.sleep(0.2)
	# GPIO.output(buzzer,GPIO.LOW)
	# time.sleep(1)
	
# while(1):
	# buzzer_alert()		          
	
