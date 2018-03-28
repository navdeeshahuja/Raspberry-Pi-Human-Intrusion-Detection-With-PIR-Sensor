import RPi.GPIO as GPIO
import time
import json, requests

AUTHORITY_PHONE_NUMBER = 8527250263
sent = False
def informAuthority():
    if sent:
        return
	link = "https://snowbarter.com/sendpranav.php?mob={}&senderId=INTRSN&message=intrusion%20detected".format(AUTHORITY_PHONE_NUMBER)
    resp = requests.get(url=link, verify=False)
    sent = True
    print("responseFromServer -> ", resp.text)

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