#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import time
import configparser
from robo_clippy import servo

config = configparser.ConfigParser()
config.read('settings.ini')

s = servo.Servo(config)

# Control via emotions (high level motions)
print("CLIPPY ANGRY!")
s.angry()
time.sleep(2)

print("CLIPPY EXCITED!")
s.excited()
time.sleep(2)

print("CLIPPY THINKING")
s.think()
time.sleep(2)

print("CLIPPY NEUTRAL")
s.neutral()
time.sleep(2)

print("CLIPPY SPEAKING")
s.speak()
time.sleep(0.5)
s.speak()
time.sleep(0.5)
s.speak()
time.sleep(0.5)
s.speak()
time.sleep(2)

print("CLIPPY WIGGLE EYES")
s.wiggle_eyes()