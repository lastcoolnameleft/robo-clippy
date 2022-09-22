# Tuning Robo-Clippy

Because Servos aren't perfect, the PWM frequences often need to be tuned.  

A lot of fine-tuning goes into getting each of the servo.MOUTH/LEFT/RIGHT* values correct.

## How to calibrate

* Disconnect servo from LEGO
* Run `servo-calibrate.py` to set everything to neutral
* Connect servo to LEGO
* Continue running `servo-calibrate.py`

## Move the servos individually

```shell
python3
from robo_clippy import servo
import configparser
from collections import OrderedDict

SETTINGS_FILE = 'settings.ini'
config = configparser.ConfigParser()
config.read(SETTINGS_FILE)
s = servo.Servo(config)

# Control via servos (lower level motions)
s.pwm.set_pwm(s.MOUTH_SERVO, 0, s.MOUTH_NEUTRAL)
s.pwm.set_pwm(s.MOUTH_SERVO, 0, s.MOUTH_HALF)
s.pwm.set_pwm(s.MOUTH_SERVO, 0, s.MOUTH_FULL)
s.pwm.set_pwm(s.LEFT_SERVO, 0, s.LEFT_UP)
s.pwm.set_pwm(s.LEFT_SERVO, 0, s.LEFT_MIDDLE)
s.pwm.set_pwm(s.LEFT_SERVO, 0, s.LEFT_DOWN)
s.pwm.set_pwm(s.RIGHT_SERVO, 0, s.RIGHT_UP)
s.pwm.set_pwm(s.RIGHT_SERVO, 0, s.RIGHT_MIDDLE)
s.pwm.set_pwm(s.RIGHT_SERVO, 0, s.RIGHT_DOWN)

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
s.wiggle_eyes()
```

