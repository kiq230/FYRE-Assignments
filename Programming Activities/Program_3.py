# This program was created in Arduino Lab for MicroPython
# Using ESP32/Nano
# For ENGR095, module Sensing the World.

# Revision of Program 2
# OBJ: Output my name with variables

import machine

# Set pins in use (set as ESP32, written as Nano)
pinA0 = machine.Pin(1, machine.Pin.OUT)

# Name var
name = "Kindah Qaissi"

print("", name) # output to REPL separating from OK