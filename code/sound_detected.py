import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
#func = GPIO.gpio_function(sensor_sound)
GPIO.setmode(GPIO.BCM)
def sound_detector():
	
	sound_prev_input = 1
	Sound = 1
	
	sensor_sound = 6
	y_led = 5
	GPIO.setup(sensor_sound, GPIO.IN)
	GPIO.setup(y_led, GPIO.OUT,initial=GPIO.HIGH)
	while True:
		sound_state = GPIO.input(sensor_sound)
		if((not sound_prev_input) and sound_state):
			Sound = (Sound+1)%2

		sound_prev_input = sound_state

		if(Sound == 1):
			GPIO.output(y_led, GPIO.HIGH)
		else:
			GPIO.output(y_led, GPIO.LOW)
		time.sleep(0.09)

#sound_detector()


