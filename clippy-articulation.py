#!/usr/bin/python3

from robo_clippy import servo, listener, audio

s = servo.Servo()
da = audio.detect.DetectAudio()
l = listener.Listener(s, da)

l.start()
