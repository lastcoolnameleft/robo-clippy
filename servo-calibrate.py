#!/usr/bin/python3

import time
from robo_clippy import servo
s = servo.Servo()

print('MOUTH_NEUTRAL=' + str(servo.MOUTH_NEUTRAL))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_NEUTRAL)
time.sleep(2)

print('MOUTH_HALF=' + str(servo.MOUTH_HALF))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_HALF)
time.sleep(2)

print('MOUTH_FULL=' + str(servo.MOUTH_FULL))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_FULL)
time.sleep(2)

print('LEFT_UP=' + str(servo.LEFT_UP))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_UP)
time.sleep(2)

print('LEFT_MIDDLE=' + str(servo.LEFT_MIDDLE))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_MIDDLE)
time.sleep(2)

print('LEFT_DOWN=' + str(servo.LEFT_DOWN))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_DOWN)
time.sleep(2)

print('RIGHT_UP=' + str(servo.RIGHT_UP))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_UP)
time.sleep(2)

print('RIGHT_MIDDLE=' + str(servo.RIGHT_MIDDLE))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_MIDDLE)
time.sleep(2)

print('RIGHT_DOWN=' + str(servo.RIGHT_DOWN))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_DOWN)
time.sleep(2)
