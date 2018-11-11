# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685
import time

MOUTH_SERVO = 0
RIGHT_SERVO = 1
LEFT_SERVO = 2

class Servo(object):

    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()
    mouth_position = 0
    thinking = False

    def __init__(self):
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)

    # THE EMOTIONS OF CLIPPY.  HE'S ALIVEEEEEEE!!!!!
    def angry(self):
        print('Clippy angry')
        self.left_eye_down()
        self.right_eye_down()

    def excited(self):
        print('Clippy excited')
        self.left_eye_up()
        self.right_eye_up()

    def think(self):
        print('Clippy think')
        if self.thinking == False:
            print('Clippy thinking 1')
            self.left_eye_up()
            self.right_eye_down()
            self.thinking = True
        elif self.thinking == True:
            print('Clippy thinking 2')
            self.left_eye_down()
            self.right_eye_up()
            self.thinking = False

    def neutral(self):
        print('Clippy neutral')
        self.left_eye_middle()
        self.right_eye_middle()
        self.mouth_neutral()
        self.thinking = False

    def speak(self):
        print('Clippy speak')
        if self.mouth_position == 0:
            print('Clippy move mouth half forward')
#            self.left_eye_middle()
#            self.right_eye_middle()
            self.mouth_forward_half()
            self.mouth_position = 1
        else:
            print('Clippy move mouth full forward')
#            self.left_eye_middle()
#            self.right_eye_middle()
            self.mouth_forward_full()
            self.mouth_position = 0

    # Everything below here should be "private"-ish
    def mouth_neutral(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 430)

    def mouth_forward_full(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 240)

    def mouth_forward_half(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, 320)

    def left_eye_up(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 395)

    def left_eye_down(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 290)

    def left_eye_middle(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, 360)

    def right_eye_up(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 380)

    def right_eye_down(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 300)

    def right_eye_middle(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, 350)