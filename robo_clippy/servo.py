# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685
import time
import random

MOUTH_SERVO = 0
RIGHT_SERVO = 1
LEFT_SERVO = 2

MOUTH_NEUTRAL = 550
MOUTH_HALF = 490
MOUTH_FULL = 430

LEFT_UP = 530
LEFT_MIDDLE = 500
LEFT_DOWN = 450

RIGHT_UP = 480
RIGHT_MIDDLE = 450
RIGHT_DOWN = 400

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
        self.mouth_position = random.choice(list(filter(lambda x: x != self.mouth_position, [0, 1, 2])))

        if self.mouth_position == 0:
            print('Clippy move mouth neutral')
            self.mouth_neutral()
        elif self.mouth_position == 1:
            print('Clippy move mouth forward half')
            self.mouth_forward_half()
        elif self.mouth_position == 2:
            print('Clippy move mouth forward full')
            self.mouth_forward_full()
        else:
            print('Unknown Clippy mouth movement' + str(self.mouth_position))

    def wiggle_eyes(self):
        print('Clippy wiggle eyes')
        sleep_time=.5
        self.left_eye_up()
        self.right_eye_up()
        time.sleep(sleep_time)

        self.left_eye_middle()
        self.right_eye_middle()
        time.sleep(sleep_time)

        self.left_eye_up()
        self.right_eye_up()
        time.sleep(sleep_time)

        self.left_eye_middle()
        self.right_eye_middle()
        time.sleep(sleep_time)

        self.left_eye_up()
        self.right_eye_up()



    # Everything below here should be "private"-ish
    def mouth_neutral(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, MOUTH_NEUTRAL)

    def mouth_forward_full(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, MOUTH_FULL)

    def mouth_forward_half(self):
        self.pwm.set_pwm(MOUTH_SERVO, 0, MOUTH_HALF)

    def left_eye_up(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, LEFT_UP)

    def left_eye_down(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, LEFT_DOWN)

    def left_eye_middle(self):
        self.pwm.set_pwm(LEFT_SERVO, 0, LEFT_MIDDLE)

    def right_eye_up(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, RIGHT_UP)

    def right_eye_down(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, RIGHT_DOWN)

    def right_eye_middle(self):
        self.pwm.set_pwm(RIGHT_SERVO, 0, RIGHT_MIDDLE)