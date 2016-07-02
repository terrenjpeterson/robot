import RPi.GPIO as GPIO
import time

elbow = 18
elbow_start_pos = 5
thumb = 23
thumb_start_pos = 20
frequency = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(elbow, GPIO.OUT)
GPIO.setup(thumb, GPIO.OUT)

print "Setup Complete"

servo1 = GPIO.PWM(elbow, frequency)
servo1.start(elbow_start_pos)

servo2 = GPIO.PWM(thumb, frequency)
servo2.start(thumb_start_pos)

print "Starting Servos"

time.sleep(2)

for x in range(0, 20):
  duty = float(x *10) / 10.0 * 5
  servo1.ChangeDutyCycle(duty)
  time.sleep(0.05)
  print duty

print "Complete Elbow Movement"

servo1.stop()

for y in range(0,10):
  duty = thumb_start_pos - float(y) / 10.0 * 5
  servo2.ChangeDutyCycle(duty)
  time.sleep(0.05)
  print duty

print "Complete Thumb Movement"

GPIO.cleanup()
