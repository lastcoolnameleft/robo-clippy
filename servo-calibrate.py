#!/usr/bin/python3

from robo_clippy import servo
s = servo.Servo()

print('MOUTH_NEUTRAL=' + str(servo.MOUTH_NEUTRAL))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_NEUTRAL)
print('MOUTH_HALF=' + str(servo.MOUTH_HALF))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_HALF)
print('MOUTH_FULL=' + str(servo.MOUTH_FULL))
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_FULL)

print('LEFT_UP=' + str(servo.LEFT_UP))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_UP)
print('LEFT_MIDDLE=' + str(servo.LEFT_MIDDLE))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_MIDDLE)
print('LEFT_DOWN=' + str(servo.LEFT_DOWN))
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_DOWN)

print('RIGHT_UP=' + str(servo.RIGHT_UP))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_UP)
print('RIGHT_MIDDLE=' + str(servo.RIGHT_MIDDLE))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_MIDDLE)
print('RIGHT_DOWN=' + str(servo.RIGHT_DOWN))
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_DOWN)
