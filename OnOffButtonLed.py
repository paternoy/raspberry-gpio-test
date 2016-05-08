import RPi.GPIO as GPIO
import time

pwm=0

class OnOffButtonLed(object):
	
	def __init__(self):
		self.butPin=16
		self.redPin=23
		self.bluePin=24
		self.greenPin=18
		self.activated=False
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(self.redPin,GPIO.OUT)
		GPIO.setup(self.bluePin,GPIO.OUT)
		GPIO.setup(self.greenPin,GPIO.OUT)
		#self.pwm = GPIO.PWM(self.bluePin, 50)
		#self.dc = 0
		GPIO.output(self.redPin,False)
		GPIO.output(self.greenPin,False)
		GPIO.output(self.bluePin,False)

	def loop(self):
		print("Starting...")
		#self.pwm.start(self.dc)
		i=0
		activated=False
		while True:
			if (GPIO.input(self.butPin)):
				self.toggle()
				print("Button Pressed")
				time.sleep(1)		
			time.sleep(0.1)
			i=i+1
			#self.dc=i%25*4
			#self.pwm.ChangeDutyCycle(self.dc)

	def refresh(self):
		GPIO.output(self.redPin,not self.activated)
		GPIO.output(self.greenPin,self.activated)
	
	def toggle(self):
		self.activated= not self.activated
		self.refresh()
