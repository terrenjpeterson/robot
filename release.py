# import GPIO library that includes the pulse width function

import RPi.GPIO as GPIO
import time

# import json library

import json

# import boto library that handles queuing functions

import boto.sqs

# connect to queue

conn = boto.sqs.connect_to_region("us-east-1")
my_queue = conn.get_queue('talkWithPitcher')

print 'queue name'
print my_queue

# check queue to see if a request exists 

incomingMsgs = my_queue.get_messages()

# if length is zero, nothing to do

print len(incomingMsgs)

# read messages

for incomingMsg in incomingMsgs:
    print incomingMsg.get_body()

# set parameters

elbow_pin = 18
elbow_range = 11
elbow_start_pos = 10

speed = 0.1
frequency = 60

# setup GPIO pins for servos

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(elbow_pin, GPIO.OUT)

print "Setup Complete"

servo1 = GPIO.PWM(elbow_pin, frequency)
servo1.start(elbow_start_pos)

print "Load Ball"

# this loop is the arc of throwing motion
for x in range(0, elbow_range):
  duty1 = elbow_start_pos - (float(x * 5) / 10.0)
  servo1.ChangeDutyCycle(duty1)
  time.sleep(speed)
  print duty1

print "Stop Throwing Movement"

time.sleep(1)
servo1.stop()

GPIO.cleanup()
