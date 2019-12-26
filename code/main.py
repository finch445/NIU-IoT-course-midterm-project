import RPi.GPIO as GPIO
import threading
import time
from alert import alert_sel
from sound_detected import sound_detector
from PotentiometerLed import photocellled
from VR_led_control import VR_led

GPIO.setmode(GPIO.BCM)

class  mode1(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print ("Starting " + self.name)
        alertmode()
        #sound_detected()
        print ("Exiting " + self.name)
 
class mode2 (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print ("Starting " + self.name)
        #alert()
        soundsw()
        print ("Exiting " + self.name)

class photocell (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ('Starting' + self.name)
		photocellmcp()
		print('Exiting' + self.name)

class VRLedControl (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print('Staring' + self.name)
        VRled()
        print('Exiting' + self.name)


def alertmode():
    #PIN_NO=29
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(PIN_NO, GPIO.OUT)
    #GPIO.output(PIN_NO,GPIO.HIGH)
    alert_sel()
    print('ok')

	
def soundsw():
    #PIN=15
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(PIN, GPIO.OUT)
    #GPIO.output(PIN,GPIO.HIGH)
    #sound_detected()
    sound_detector()
    print('ok!')

def photocellmcp():

	photocellled()

def VRled():

    VR_led()

# 创建新线程
thread1 = mode1(1, "mode1_on", 1)
thread2 = mode2(2, "mode2_on", 2)
thread3 = photocell(3, 'mcp3008 start', 3)
thread4 = VRLedControl(4, 'mode 4 on', 4)


# 开启线程

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
 
print ("Exiting Main Thread")
time.sleep(20)
GPIO.cleanup()

