# Team member names: Kindah, Cal, Meghan
# Purpose of code: Move servo 180 degrees on switch depress
# Date code was started: 9.16.2026
# Date of last update: 9.16.2026
# Explanation of AI use: Was used to generate the program, troubleshoot

# ==============================================================================

import time
from machine import Pin, PWM

# Setup Push Button on Pin D2 (GPIO 5) with internal pull-up resistor
BUTTON_PIN = 5
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Setup Servo PWM on Pin D3 (GPIO 6) at 50 Hz
SERVO_PIN = 6
servo = PWM(Pin(SERVO_PIN))
servo.freq(50)

# ==============================================================================
# PWM CALIBRATION VALUES (16-bit resolution: 0 - 65535)
# Frequency = 50Hz (20ms period)
# - 0 degrees   => ~0.5ms pulse = (0.5 / 20) * 65535 = 1638 duty
# - 180 degrees => ~2.4ms pulse = (2.4 / 20) * 65535 = 7864 duty
# ==============================================================================
DUTY_0_DEG = 1638
DUTY_180_DEG = 7864

# Start at 0 degrees
servo.duty_u16(DUTY_0_DEG)

print("Starting Servo Test...")
previous_state = button.value()

while True:
    current_state = button.value()

    if current_state != previous_state:
        # Switch Depressed (Pin pulled LOW to GND)
        if current_state == 0:
            print("Switch Depressed -> Moving to 180°")
            servo.duty_u16(DUTY_180_DEG)
            
        # Switch Released (Pin pulled HIGH)
        else:
            print("Switch Released -> Returning to 0°")
            servo.duty_u16(DUTY_0_DEG)

        previous_state = current_state

    time.sleep_ms(20)