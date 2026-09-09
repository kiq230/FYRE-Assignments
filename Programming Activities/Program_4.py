# This program was created in Arduino Lab for MicroPython
# Using ESP32/Nano
# For ENGR095, module Sensing the World.

# OBJ: Make an LED blink

# Modules
import machine
import time

# Set pins in use (ESP32/Nano)
led_g = machine.Pin(0, machine.Pin.OUT) # A0

# Main
while True:
  led_g.value(1)
  time.sleep(1)
  led_g.value(0)
  time.sleep(1)