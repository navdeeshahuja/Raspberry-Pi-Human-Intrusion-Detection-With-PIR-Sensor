import RPi.GPIO as GPIO
import time

AUTHORITY_PHONE_NUMBER = 8527250263

def informAuthority():
	# inform authority here
	pass

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            print("Person Detected...")
            informAuthority()
            time.sleep(2) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()