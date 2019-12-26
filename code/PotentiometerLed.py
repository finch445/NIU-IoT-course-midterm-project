# Importing modules
#import spidev # To communicate with SPI devices
from numpy import interp	# To scale values
from time import sleep	# To add delay
import RPi.GPIO as GPIO	# To use GPIO pins
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


GPIO.setwarnings(False)
# Initializing LED pin as OUTPUT pin
led_pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Creating a PWM channel at 100Hz frequency
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0) 


def photocellled():
	try:
		while True:
			output = mcp.read_adc(0)
			output = interp(output, [0, 1023], [0, 100])
			#print(output)
			pwm.ChangeDutyCycle(output)
			sleep(0.1)
	except KeyboardInterrupt:
		GPIO.cleanup()

#photocellled()