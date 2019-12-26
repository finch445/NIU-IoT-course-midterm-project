import RPi.GPIO as GPIO
import time
import sys
from led_flash import red, green
from buzzer_sound import buzzer_on
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def alert_on():
	
		#GPIO.setmode(GPIO.BCM)
	r_led = 22
	g_led = 23
	sensor_PIR = 17
	buttonPin = 13
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(sensor_PIR, GPIO.IN)
	GPIO.setup(r_led, GPIO.OUT)
	GPIO.setup(g_led, GPIO.OUT)
	input_state = GPIO.input(sensor_PIR)
	button_state = GPIO.input(buttonPin)
		#print('%d'%(button_state))
	#if(button_state == False):
		#raise IOError
	if(input_state == True):
		print('Motion Detected')
		red()
		buzzer_on()
			#time.sleep(1)
	else:
		GPIO.output(r_led, GPIO.HIGH)
		GPIO.output(g_led, GPIO.LOW)


def alert_off():
	
		#GPIO.setmode(GPIO.BCM)
	r_led = 22
	g_led = 23
	sensor_PIR = 17
	buttonPin = 13
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(sensor_PIR, GPIO.IN)
	GPIO.setup(r_led, GPIO.OUT)
	GPIO.setup(g_led, GPIO.OUT)
	input_state = GPIO.input(sensor_PIR)
	button_state = GPIO.input(buttonPin)
		#print('%d'%(button_state))
		#if(button_state == False):
			#raise IOError
	if(input_state == True):
		print('Motion Detected')
		green()
			#time.sleep(1)
	else:
		GPIO.output(r_led, GPIO.LOW)
		GPIO.output(g_led, GPIO.HIGH)