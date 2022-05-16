import RPi.GPIO as GPIO
import time
import sys

LEDPIN = 26
SWITCH_PIN = 16
switch_state = 0
is_pushing = 0
end_time = time.time()
args = sys.argv
on_timer = args[1] if args[1] else 3
off_timer = args[2] if args[2] else 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
  while True:
    switch_state = GPIO.input(SWITCH_PIN)
    if switch_state == 0 and is_pushing == 0:
      timer = off_timer if GPIO.input(LEDPIN) else on_timer
      end_time = time.time() + int(timer)
      is_pushing = 1
    elif switch_state == 0 and is_pushing == 1:
      if end_time <= time.time():
        GPIO.output(LEDPIN, not GPIO.input(LEDPIN))
        is_pushing = -1
    else:
      is_pushing = 0
      
except KeyboardInterrupt:
  pass

GPIO.cleanup()