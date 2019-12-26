import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def buzzer_on():
	#GPIO.setmode(GPIO.BCM)	
	buzzer = 27
	GPIO.setup(buzzer, GPIO.OUT)
	p = GPIO.PWM(buzzer, 50)
	p.start(25)
	p.ChangeFrequency(770)
	time.sleep(0.5)
	p.ChangeFrequency(960)
	time.sleep(0.5)
	p.stop()
	GPIO.cleanup()
