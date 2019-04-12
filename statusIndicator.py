import I2C_LCD_driver

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

class status:

	def Internet(self, i):
		lcd.lcd_display_string("I",1,15)
		if i == 0: #indicador false
			lcd.lcd_load_custom_chars(customC)
			lcd.lcd_write(144)
			lcd.lcd_write_char(0)
		elif i == 1: #indicador true
			lcd.lcd_load_custom_chars(customC)
			lcd.lcd_write(144)
			lcd.lcd_write_char(1)

	def Server(self, i):
		lcd.lcd_display_string("S",1,18)
		if i == 0: #indicador false
			lcd.lcd_load_custom_chars(customC)
			lcd.lcd_write(147)
			lcd.lcd_write_char(0)
		elif i == 1: #indicador true
			lcd.lcd_load_custom_chars(customC)
			lcd.lcd_write(147)
			lcd.lcd_write_char(1)
			
			
