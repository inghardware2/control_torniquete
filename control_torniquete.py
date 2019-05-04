import I2C_LCD_driver
import statusIndicator
from datetime import datetime
import RPi.GPIO as GPIO
import time
import sys

#pin configuration
buzzer = 22
relayIN = 27
#relayOUT = 15

#port configuration
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initial states
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)
GPIO.setup(relayIN,GPIO.OUT)
GPIO.output(relayIN,GPIO.LOW)

#object statement
lcd = I2C_LCD_driver.lcd()
stateServices = statusIndicator.status() 

#active buzzer
def buzzer_active():
	for x in range(3):
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(0.1)
        
#preloaded messages
def show_lcd(a):
	if a == 0:
	 lcd.lcd_clear() 
	 lcd.lcd_display_string("DENEGADO",2,6)
	 timeString = datetime.now().strftime('%H:%M:%S')
	 lcd.lcd_display_string(timeString,3,6)
	 
	elif a == 1:
	 	if len(sys.argv) == 5:
			lcd.lcd_clear() 	
			lcd.lcd_display_string("BIENVENIDO",1,5)
			timeString = datetime.now().strftime('%H:%M:%S')
			lcd.lcd_display_string(timeString,2,6)
			lcd.lcd_display_string("DIAS RESTANTES: " + sys.argv[4],4,0)
		else:
			lcd.lcd_clear() 	
			lcd.lcd_display_string("BIENVENIDO",2,5)
			timeString = datetime.now().strftime('%H:%M:%S')
			lcd.lcd_display_string(timeString,3,6)
		
	elif a == 2:
		lcd.lcd_clear()    
		dateString = datetime.now().strftime('%d/%m/%y')
		lcd.lcd_display_string(dateString, 1,0)
		lcd.lcd_display_string("COLOQUE SU HUELLA",3,1)
     
#access deneid
if int(sys.argv[1]) == 0:
	show_lcd(0)
	buzzer_active()	
		          
    
#access grented 
if int(sys.argv[1]) == 1:
        show_lcd(1)
        GPIO.output(relayIN,GPIO.HIGH)
        time.sleep(3)
        GPIO.output(relayIN,GPIO.LOW) 
            
#return time     
time.sleep(1)

#initial message
show_lcd(2)

#state indicators
#Internet
if int(sys.argv[2]) == 0:
	stateServices.Internet(0)  
elif int(sys.argv[2]) == 1:
	stateServices.Internet(1)   
#Server    
if int(sys.argv[3]) == 0:
	stateServices.Server(0)  
elif int(sys.argv[3]) == 1:
	stateServices.Server(1)   
GPIO.cleanup()   
