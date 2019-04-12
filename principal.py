import I2C_LCD_driver
import statusIndicator
from datetime import datetime
import RPi.GPIO as GPIO
import time
import sys

#configuración de pines
buzzer = 17
relayIN = 27
relayOUT = 15

#configuración de puerto
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#estados iniciales
GPIO.setup(buzzer,GPIO.OUT)
GPIO.output(buzzer,GPIO.LOW)
GPIO.setup(relayIN,GPIO.OUT)
GPIO.output(relayIN,GPIO.LOW)
GPIO.setup(relayOUT,GPIO.OUT)
GPIO.output(relayOUT,GPIO.LOW)

#declaración de clases
lcd = I2C_LCD_driver.lcd()
stateServices = statusIndicator.status() 

#función que define la activación y tiempo del buzzer
def buzzer_active():
	for x in range(3):
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(0.3)
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(0.1)
        
#función de mensajes preestablecidos
def show_lcd(a):
	if a == 0:
	 lcd.lcd_clear() 
	 lcd.lcd_display_string("DENEGADO",1,6)
	
	elif a == 1:
	 #lcd.lcd_clear()
	 lcd.lcd_display_string("BIENVENIDO",2,5)
	 timeString = datetime.now().strftime('%H:%M:%S')
	 lcd.lcd_display_string(timeString,3,6)
		
	elif a == 2:
	 lcd.lcd_clear()    
	 dateString = datetime.now().strftime('%d/%m/%y')
	 lcd.lcd_display_string(dateString, 1,0)
	 lcd.lcd_display_string("COLOQUE SU HUELLA",3,1)
     
#Acceso denegado muestro emnsaje de error
if int(sys.argv[1]) == 0:
	show_lcd(0)
	if len(sys.argv[4]) > 0:
		c = (20 - len(sys.argv[4])) / 2
		for elements in sys.argv[4]:				
			lcd.lcd_display_string(elements,3,c)	
			c=c+1
	buzzer_active()		
	time.sleep(1)          
    
#Acceso concedido, habilito torniquete    
if int(sys.argv[1]) == 1:
        show_lcd(1)
        GPIO.output(relayIN,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(relayIN,GPIO.LOW) 
            
#tiempo de regreso      
time.sleep(1)

#mensaje inicial
show_lcd(2)

#estado de los indicadores de internet y servidor
if int(sys.argv[2]) == 0:
	stateServices.Internet(0)  
elif int(sys.argv[2]) == 1:
	stateServices.Internet(1)   
    
if int(sys.argv[3]) == 0:
	stateServices.Server(0)  
elif int(sys.argv[3]) == 1:
	stateServices.Server(1)   
    
    
