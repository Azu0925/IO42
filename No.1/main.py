import RPi.GPIO as GPIO
import time

LEDPIN = 26
SWITCH_PIN = 16
switch_state = 0
is_pushing = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
  while True:
    swtich_state = GPIO.input(SWITCH_PIN)
    if swtich_state == 0 and is_pushing == False:
      GPIO.output(LEDPIN, GPIO.HIGH)
      # GPIO.output(LEDPIN_2, not GPIO.input(LEDPIN_2))
      is_pushing = True
    elif swtich_state == 0 and is_pushing == True:
      GPIO.output(LEDPIN, GPIO.HIGH)
      is_pushing = True
    else:
      GPIO.output(LEDPIN, GPIO.LOW)
      is_pushing = False
    time.sleep(0.1)


except KeyboardInterrupt:
  pass

GPIO.cleanup()