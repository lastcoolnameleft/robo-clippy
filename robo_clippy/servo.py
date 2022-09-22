# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division

# Import the PCA9685 module.
import Adafruit_PCA9685
import time
import random
import logging
import configparser

class MockPCA9685():
    def set_pwm_freq(self, unused):
        return True

    def set_pwm(self, unused1, unused2, unused3):
        return True

class Servo(object):

    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()
    #pwm = MockPCA9685()

    mouth_position = 0
    thinking = False

    def __init__(self, config):
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)
        self.MOUTH_SERVO = int(config['SERVO']['MOUTH_SERVO'])
        self.RIGHT_SERVO = int(config['SERVO']['RIGHT_SERVO'])
        self.LEFT_SERVO = int(config['SERVO']['LEFT_SERVO'])
        
        self.MOUTH_NEUTRAL = int(config['SERVO']['MOUTH_NEUTRAL'])
        self.MOUTH_HALF = int(config['SERVO']['MOUTH_HALF'])
        self.MOUTH_FULL = int(config['SERVO']['MOUTH_FULL'])

        self.LEFT_MIDDLE = int(config['SERVO']['LEFT_MIDDLE'])
        self.LEFT_UP = int(config['SERVO']['LEFT_UP'])
        self.LEFT_DOWN = int(config['SERVO']['LEFT_DOWN'])

        self.RIGHT_MIDDLE = int(config['SERVO']['RIGHT_MIDDLE'])
        self.RIGHT_UP = int(config['SERVO']['RIGHT_UP'])
        self.RIGHT_DOWN = int(config['SERVO']['RIGHT_DOWN'])

    # THE EMOTIONS OF CLIPPY.  HE'S ALIVEEEEEEE!!!!!
    def angry(self):
        logging.info('Clippy angry')
        self.left_eye_down()
        self.right_eye_down()

    def excited(self):
        logging.info('Clippy excited')
        self.left_eye_up()
        self.right_eye_up()

    def think(self):
        logging.info('Clippy think')
        if self.thinking == False:
            logging.debug('Clippy thinking 1')
            self.left_eye_up()
            self.right_eye_down()
            self.thinking = True
        elif self.thinking == True:
            logging.debug('Clippy thinking 2')
            self.left_eye_down()
            self.right_eye_up()
            self.thinking = False

    def neutral(self):
        logging.info('Clippy neutral')
        self.left_eye_middle()
        self.right_eye_middle()
        self.mouth_neutral()
        self.thinking = False

    def speak(self):
        logging.debug('Clippy speak')
        self.mouth_position = random.choice(list(filter(lambda x: x != self.mouth_position, [0, 1, 2])))

        if self.mouth_position == 0:
            logging.debug('Clippy move mouth neutral')
            self.mouth_neutral()
        elif self.mouth_position == 1:
            logging.debug('Clippy move mouth forward half')
            self.mouth_forward_half()
        elif self.mouth_position == 2:
            logging.debug('Clippy move mouth forward full')
            self.mouth_forward_full()
        else:
            logging.warn('Unknown Clippy mouth movement' + str(self.mouth_position))

    def wiggle_eyes(self):
        logging.info('Clippy wiggle eyes')
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
        self.pwm.set_pwm(self.MOUTH_SERVO, 0, self.MOUTH_NEUTRAL)

    def mouth_forward_full(self):
        self.pwm.set_pwm(self.MOUTH_SERVO, 0, self.MOUTH_FULL)

    def mouth_forward_half(self):
        self.pwm.set_pwm(self.MOUTH_SERVO, 0, self.MOUTH_HALF)

    def left_eye_up(self):
        self.pwm.set_pwm(self.LEFT_SERVO, 0, self.LEFT_UP)

    def left_eye_down(self):
        self.pwm.set_pwm(self.LEFT_SERVO, 0, self.LEFT_DOWN)

    def left_eye_middle(self):
        self.pwm.set_pwm(self.LEFT_SERVO, 0, self.LEFT_MIDDLE)

    def right_eye_up(self):
        self.pwm.set_pwm(self.RIGHT_SERVO, 0, self.RIGHT_UP)

    def right_eye_down(self):
        self.pwm.set_pwm(self.RIGHT_SERVO, 0, self.RIGHT_DOWN)

    def right_eye_middle(self):
        self.pwm.set_pwm(self.RIGHT_SERVO, 0, self.RIGHT_MIDDLE)