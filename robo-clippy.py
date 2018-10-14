# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

mouth_servo = 0
right_servo = 1
left_servo = 2

right_servo_max = 395
right_servo_max = 385
left_servo_min = 300
right_sero_min = 300

def angry():
    pwm.set_pwm(right_servo, 0, 300)
    pwm.set_pwm(left_servo, 0, 300)

def excited():
    pwm.set_pwm(right_servo, 0, 385)
    pwm.set_pwm(left_servo, 0, 395)

def confused():
    pwm.set_pwm(right_servo, 0, 385)
    pwm.set_pwm(left_servo, 0, 325)

while True:
    excited()
    time.sleep(1)
    confused()
    time.sleep(1)
    angry()
    time.sleep(1)

