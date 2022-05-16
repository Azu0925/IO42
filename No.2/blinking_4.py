import RPi.GPIO as GPIO
import time

LEDPIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
pi = GPIO.PWM(LEDPIN, 45)
pi.start(50)

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  pass

pi.stop()
GPIO.cleanup()
