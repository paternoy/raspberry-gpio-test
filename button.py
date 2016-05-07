import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
butPin=16
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("vamo")

while True:
	if (GPIO.input(butPin)):
		print("Button Pressied")
	time.sleep(0.05)
