import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def mcp3008photo():
	while True:
		val = mcp.read_adc(0)
		print('val = %d'%(val))
		time.sleep(1)

#mcp3008photo()