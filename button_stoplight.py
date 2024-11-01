import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#^^ This is just inputting the libraries 


buttonpin = 21

GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #

GPIO.output(6,GPIO.LOW)
GPIO.output(26,GPIO.LOW)

def lights():
	print ("GREEN LED on")
	GPIO.output(6,GPIO.HIGH)
	GPIO.output(26,GPIO.LOW)
	time.sleep(2)
	print("Yellow LED on")
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	time.sleep(2)
	print ("RED LED on")
	GPIO.output(26,GPIO.HIGH)
	GPIO.output(6,GPIO.LOW)
	time.sleep(2)
	GPIO.output(26,GPIO.LOW)


while True:
	if GPIO.input(buttonpin) == GPIO.LOW:
		lights()
