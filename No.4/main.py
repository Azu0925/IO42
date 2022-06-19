import RPi.GPIO as GPIO
import Light

LEDPIN_BLUE = 26
LEDPIN_RED = 6
LEDPIN_YELLOW = 5
SWITCH_PIN = 16
on_delay = 0
off_delay = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN_BLUE, GPIO.OUT)
GPIO.setup(LEDPIN_RED, GPIO.OUT)
GPIO.setup(LEDPIN_YELLOW, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
blue_led = Light.Light(LEDPIN_BLUE, False, 1)
red_led = Light.Light(LEDPIN_RED, False, 1)
yellow_led = Light.Light(LEDPIN_YELLOW, False, 1)


try:
  while True:
    blue_led.switch_state = GPIO.input(SWITCH_PIN)
    red_led.switch_state = GPIO.input(SWITCH_PIN)
    yellow_led.switch_state = GPIO.input(SWITCH_PIN)
    blue_led.momentary()
    red_led.momentary(on_delay_time=2, off_delay_time=3)
    yellow_led.alternate(on_delay_time=2, off_delay_time=3)
    
    if blue_led.light_state:
      GPIO.output(blue_led.LED_PIN, GPIO.HIGH)
    else:
      GPIO.output(blue_led.LED_PIN, GPIO.LOW)

    if red_led.light_state:
      GPIO.output(red_led.LED_PIN, GPIO.HIGH)
    else:
      GPIO.output(red_led.LED_PIN, GPIO.LOW)

    if yellow_led.light_state:
      GPIO.output(yellow_led.LED_PIN, GPIO.HIGH)
    else:
      GPIO.output(yellow_led.LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
  pass

GPIO.cleanup()