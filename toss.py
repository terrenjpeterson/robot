# import GPIO library that includes the pulse width function

import RPi.GPIO as GPIO
import time

# set parameters

elbow = 18
elbow_start_pos = 5
elbow_range = 25

speed = 0.02
frequency = 100

# setup GPIO pins for servos

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(elbow, GPIO.OUT)

print "Setup Complete"

time.sleep(1)

servo1 = GPIO.PWM(elbow, frequency)
servo1.start(elbow_start_pos)

print "Load Ball"

time.sleep(2)

# this loop is the arc of throwing motion
for x in range(0, elbow_range):
  duty = elbow_start_pos + (float(x * 10) / 10.0)
  servo1.ChangeDutyCycle(duty)
  time.sleep(speed)
  print duty

print "Stop Throwing Movement"

servo1.stop()

GPIO.cleanup()
