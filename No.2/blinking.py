import RPi.GPIO as GPIO
import time

LEDPIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)

try:
  while True:
    GPIO.output(LEDPIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDPIN, GPIO.LOW)
    time.sleep(0.5)
except KeyboardInterrupt:
  pass

GPIO.cleanup()