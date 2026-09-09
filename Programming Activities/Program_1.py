# This program was created in Arduino Lab for MicroPython
# Using ESP32/Nano
# For ENGR095, module Sensing the World.

# OBJ: Output "Hello World"

import machine

# Set pins in use (set as ESP32, written as Nano)
pinA0 = machine.Pin(1, machine.Pin.OUT)

print("","Hello World") # output to REPL separating from OK
