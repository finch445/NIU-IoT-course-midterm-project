import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def red():
	GPIO.setmode(GPIO.BCM)
	r_led = 22
	GPIO.setup(r_led, GPIO.OUT, initial=GPIO.LOW)
	GPIO.output(r_led, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(r_led, GPIO.LOW)
	#time.sleep(1)

def green():
	GPIO.setmode(GPIO.BCM)
	g_led = 23
	GPIO.setup(g_led, GPIO.OUT, initial=GPIO.LOW)
	GPIO.output(g_led, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(g_led, GPIO.LOW)
	time.sleep(1)