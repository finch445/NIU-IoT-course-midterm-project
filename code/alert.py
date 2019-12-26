import RPi.GPIO as GPIO
import time
import sys
from secure import alert_on, alert_off
GPIO.setmode(GPIO.BCM)
def alert_sel():
	prev_input = 1
	Light = 1
	
	try:
		while True:
			GPIO.setmode(GPIO.BCM)
			buttonPin = 13
			GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
			input_state = GPIO.input(buttonPin)

			if((not prev_input) and input_state):
				Light = (Light+1)%2

			prev_input = input_state

			if(Light == 1):
				alert_on()
			
			else:
				alert_off()
			
			time.sleep(0.09)

	except KeyboardInterrupt:
		GPIO.cleanup()

#alert_sel()
