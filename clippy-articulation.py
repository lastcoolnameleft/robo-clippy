from robo_clippy import servo, listener
import time

s = servo.Servo()
l = listener.Listener(s)

l.start()