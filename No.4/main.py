import RPi.GPIO as GPIO
import Light

LEDPIN = 26
LEDPIN_RED = 6
SWITCH_PIN = 16
on_delay = 0
off_delay = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
blue_led = Light.Light(LEDPIN, False, 1)
red_led = Light.Light(LEDPIN_RED, False, 1)

try:
  while True:
    blue_led.switch_state = GPIO.input(SWITCH_PIN)
    blue_led.alternate(on_delay_time=2, off_delay_time=3)
    
    if blue_led.light_state:
      GPIO.output(blue_led.LED_PIN, GPIO.HIGH)
    else:
      GPIO.output(blue_led.LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
  pass

GPIO.cleanup()