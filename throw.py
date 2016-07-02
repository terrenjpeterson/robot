import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)

print "Setup Complete"

pwm = GPIO.PWM(23, 100)
pwm.start(5)

print "Starting"

time.sleep(2)

for x in range(0, 30):
  duty = float(x *10) / 10.0 * 5
  pwm.ChangeDutyCycle(duty)
  time.sleep(0.03)
  print duty

print "Complete"

pwm.stop()
GPIO.cleanup()
