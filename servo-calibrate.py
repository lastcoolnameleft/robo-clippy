#!/usr/bin/python3

import configparser
from collections import OrderedDict
from robo_clippy import servo

SETTINGS_FILE = 'settings.ini'
config = configparser.ConfigParser()
config.read(SETTINGS_FILE)
s = servo.Servo(config)

positions = OrderedDict()
positions['MOUTH_HALF'] = {'servo': s.MOUTH_SERVO, 'frequency': s.MOUTH_HALF}
positions['MOUTH_FULL'] = {'servo': s.MOUTH_SERVO, 'frequency': s.MOUTH_FULL}
positions['LEFT_UP'] = {'servo': s.LEFT_SERVO, 'frequency': s.LEFT_UP}
positions['LEFT_DOWN'] = {'servo': s.LEFT_SERVO, 'frequency': s.LEFT_DOWN}
positions['RIGHT_UP'] = {'servo': s.RIGHT_SERVO, 'frequency': s.RIGHT_UP}
positions['RIGHT_DOWN'] = {'servo': s.RIGHT_SERVO, 'frequency': s.RIGHT_DOWN}

print("Setting everything to neutral")
print('Setting: MOUTH at frequency ' + str(s.MOUTH_NEUTRAL))
s.pwm.set_pwm(s.MOUTH_SERVO, 0, s.MOUTH_NEUTRAL)
print('Setting: LEFT EYEBROW at frequency ' + str(s.LEFT_MIDDLE))
s.pwm.set_pwm(s.LEFT_SERVO, 0, s.LEFT_MIDDLE)
print('Setting: RIGHT EYEBROW at frequency ' + str(s.RIGHT_MIDDLE))
s.pwm.set_pwm(s.RIGHT_SERVO, 0, s.RIGHT_MIDDLE)
input("Press enter to begin test")

for position in positions:
    servo_id = positions[position]['servo']
    frequency = positions[position]['frequency']
    print('Testing: ' + position + ' at frequency ' + str(frequency) + ".", end =" ")
    s.pwm.set_pwm(servo_id, 0, frequency)
    override = input(" Override? ")

    while override.isdigit():
        new_frequency = int(override)
        print("setting config['SERVO'][" + position + "] = " + override)
        config['SERVO'][position] = override
        print('Testing: ' + position + ' at frequency ' + str(new_frequency) + ".", end =" ")
        s.pwm.set_pwm(servo_id, 0, int(new_frequency))
        override = input(" Override? ")

with open(SETTINGS_FILE, 'w') as configfile:
    config.write(configfile)
