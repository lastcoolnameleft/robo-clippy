# Tuning Robo-Clippy

Because Servos aren't perfect, you might need to modify individual values.  This is designed to help test each arciulation.

A lot of fine-tuning goes into getting each of the servo.MOUTH/LEFT/RIGHT* values correct.

## Test the servos
```shell
python3
from robo_clippy import servo
s = servo.Servo()

# Control via servos (lower level motions)
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_NEUTRAL)
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_HALF)
s.pwm.set_pwm(servo.MOUTH_SERVO, 0, servo.MOUTH_FULL)
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_UP)
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_MIDDLE)
s.pwm.set_pwm(servo.LEFT_SERVO, 0, servo.LEFT_DOWN)
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_UP)
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_MIDDLE)
s.pwm.set_pwm(servo.RIGHT_SERVO, 0, servo.RIGHT_DOWN)

# Control via motions (mid level motions)
s.mouth_neutral()
s.mouth_forward_full()
s.mouth_forward_half()
s.left_eye_up()
s.left_eye_down()
s.left_eye_middle()
s.right_eye_up()
s.right_eye_down()
s.right_eye_middle()

# Control via emotions (high level motions)
s.angry()
s.excited()
s.think()
s.neutral()
s.speak()
```