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

MOUTH_SERVO = 0
RIGHT_SERVO = 1
LEFT_SERVO = 2


def angry():
    pwm.set_pwm(RIGHT_SERVO, 0, 300)
    pwm.set_pwm(LEFT_SERVO, 0, 300)

def excited():
    pwm.set_pwm(RIGHT_SERVO, 0, 385)
    pwm.set_pwm(LEFT_SERVO, 0, 395)

def confused():
    pwm.set_pwm(RIGHT_SERVO, 0, 385)
    pwm.set_pwm(LEFT_SERVO, 0, 325)

def mouth_neutral():
    pwm.set_pwm(MOUTH_SERVO, 0, 380)

def mouth_forward():
    pwm.set_pwm(MOUTH_SERVO, 0, 240)

def mouth_back():
    pwm.set_pwm(MOUTH_SERVO, 0, 420)

while True:
    excited()
    time.sleep(1)
    confused()
    time.sleep(1)
    angry()
    time.sleep(1)
