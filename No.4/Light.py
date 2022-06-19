import time

class Light: 
  def __init__(self, led_pin, light_state, switch_state):
    self.LED_PIN = led_pin
    self.light_state = light_state
    self.switch_state = switch_state
    self.on_delay_timer = None
    self.off_delay_timer = None
    self.is_pushing = False

  def momentary(self, on_delay_time=0, off_delay_time=0): 
    if self.switch_state == 1 and self.is_pushing == False:
      self.on_delay_timer = time.time() + on_delay_time
      self.is_pushing = True
      self.off_delay_timer = None
    elif self.switch_state == 1 and self.is_pushing == True:
      pass
    else:
      if self.off_delay_timer is None:
        self.off_delay_timer = time.time() + off_delay_time
      self.on_delay_timer = None
      self.is_pushing = False

    if self.on_delay_timer is None:
      if self.off_delay_timer is None:
        pass
      elif self.off_delay_timer <= time.time():
        self.light_state = False
    elif self.on_delay_timer <= time.time():
      self.light_state = True
    else:
      if self.off_delay_timer is None:
        pass
      elif self.off_delay_timer <= time.time():
        self.light_state = False

  def alternate(self, on_delay_time=0, off_delay_time=0):
    if self.switch_state == 1 and self.is_pushing == False and self.light_state == False:
      print('??')
      self.on_delay_timer = time.time() + on_delay_time 
      self.is_pushing = True
    elif self.switch_state == 1 and self.is_pushing == False and self.light_state == True:
      print('##')
      self.off_delay_timer = time.time() + off_delay_time
      self.is_pushing = True
    elif self.switch_state == 1 and self.is_pushing == True:
      print('--')
      pass
    elif self.switch_state == 0 and self.is_pushing == True:
      print('離した')
      self.is_pushing = False

    if self.on_delay_timer is not None:
      if self.on_delay_timer <= time.time():
        self.light_state = True
        self.on_delay_timer = None

    if self.off_delay_timer is not None:
      if self.off_delay_timer <= time.time():
        self.light_state = False
        self.off_delay_timer = None