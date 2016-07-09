# import GPIO library that includes the pulse width function

import RPi.GPIO as GPIO
import time

# set parameters

relay_pin = 12

# setup

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay_pin, GPIO.OUT)

print "Relay Running"

#GPIO.output(relay_pin, GPIO.HIGH)
GPIO.output(relay_pin, 1)
print GPIO.HIGH

# pause

time.sleep(10)

print "Relay Off"

#GPIO.output(relay_pin, GPIO.LOW)
GPIO.output(relay_pin, 0)
print GPIO.LOW

GPIO.cleanup()
