import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
butPin=16
redPin=23
bluePin=24
greenPin=18
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(redPin,GPIO.OUT)
#GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)


print("Starting...")
try:
	i=0
	activated=False
	while True:
		if (GPIO.input(butPin)):
			activated= not activated
			print("Button Pressed")
			GPIO.output(redPin,not activated)
			GPIO.output(greenPin,activated)
			time.sleep(1)		
		time.sleep(0.1)
		#GPIO.output(redPin,i%4==0)
		#GPIO.output(bluePin,i%4==1)
		i=i+1
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	GPIO.cleanup() # cleanup all GPIO
