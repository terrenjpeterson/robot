import RPi.GPIO as GPIO
import time

elbow = 18
elbow_start_pos = 5
elbow_range = 25
thumb = 23
thumb_open_pos = 15
thumb_start_pos = 20
speed = 0.05
frequency = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(elbow, GPIO.OUT)
GPIO.setup(thumb, GPIO.OUT)

print "Setup Complete"

servo2 = GPIO.PWM(thumb, frequency)
servo2.start(thumb_open_pos)

time.sleep(2)

servo2.ChangeDutyCycle(thumb_start_pos)

time.sleep(2)

servo1 = GPIO.PWM(elbow, frequency)
servo1.start(elbow_start_pos)

print "Starting Servos"

time.sleep(5)

for x in range(0, elbow_range):
  duty = elbow_start_pos + float(x *10) / 10.0 * 1
  servo1.ChangeDutyCycle(duty)
  time.sleep(speed)
  print duty

print "Complete Elbow Movement"

servo1.stop()

for y in range(0,10):
  duty = thumb_start_pos - float(y) / 10.0 * 5
  servo2.ChangeDutyCycle(duty)
  time.sleep(speed)
  print duty

print "Complete Thumb Movement"

servo2.stop()

GPIO.cleanup()
