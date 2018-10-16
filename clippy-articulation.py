from robo_clippy import servo
import time

s = servo.Servo()

while True:
    s.neutral()
    time.sleep(2)
    s.excited()
    time.sleep(2)
    s.confused()
    time.sleep(2)
    s.angry()
    time.sleep(2)