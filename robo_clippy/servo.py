# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

MOUTH_SERVO = 0
RIGHT_SERVO = 1
LEFT_SERVO = 2

class Servo(object):

    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()

    def __init__(self):
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)


    def angry(self):
        print('Clippy angry')
        self.left_eye_down()
        self.right_eye_down()

    def excited(self):
        print('Clippy excited')
        self.left_eye_up()
        self.right_eye_up()

    def confused(self):
        print('Clippy confused')
        self.left_eye_up()
        self.right_eye_down()

    def neutral(self):
        print('Clippy neutral')
        self.left_eye_middle()
        self.right_eye_middle()

    def mouth_middle(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 380)

    def mouth_forward(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 240)

    def mouth_back(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 420)

    def left_eye_up(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 395)

    def left_eye_down(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 320)

    def left_eye_middle(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 371)

    def right_eye_up(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 380)

    def right_eye_down(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 300)

    def right_eye_middle(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 350)