import random
import drivers
from time import sleep
import RPi.GPIO as GPIO

display = drivers.Lcd()

def button_callback(channel):
	display.lcd_clear()
	
	with open('/home/pi/Dinner-Roulette-Pi/dinners.txt') as f:
		lines = f.readlines()
	
	x=0
	for dinner in lines:
		lines[x] = dinner.strip()
		x+=1


	rand = random.randrange(len(lines))
	choice = lines[rand]
	sleep(0.5)
	for x in range(3):
		long_string(display, "Dinner Roulette!", 1)
		long_string(display, choice, 2)
	sleep(30)	
	display.lcd_clear()
	display.lcd_display_string("Dinner Roulette!",1)

def long_string(display, text='', num_line=1, num_cols=16):
	if len(text) > num_cols:
		display.lcd_display_string(text[:num_cols], num_line)
		sleep(1)
		for i in range(len(text) - num_cols + 1):
			text_to_print = text[i:i+num_cols]
			display.lcd_display_string(text_to_print, num_line)
			sleep(0.4)
		sleep(1)
	else:
		display.lcd_display_string(text, num_line)

display.lcd_clear()
long_string(display, "Dinner Roulette!", 1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback,bouncetime=1000)
message = input("Press enter to quit\n\n")

#while True:
#	x = 0
display.lcd_clear()
display.lcd_display_string("Dinner Roulette!",1)
GPIO.cleanup()