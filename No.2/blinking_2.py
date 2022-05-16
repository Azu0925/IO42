# 2と3かねてる

import RPi.GPIO as GPIO
import time
import sys

LEDPIN = 26
args = sys.argv
on_sleep = args[0] if args[0] else 0.04
off_sleep = args[1] if args[1] else 0.06

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)



try:
  while True:
    GPIO.output(LEDPIN, GPIO.HIGH)
    time.sleep(on_sleep)
    GPIO.output(LEDPIN, GPIO.LOW)
    time.sleep(off_sleep)
except KeyboardInterrupt:
  pass

GPIO.cleanup()