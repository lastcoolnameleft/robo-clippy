#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import os
import sys
import logging
import time

from robo_clippy import servo
s = servo.Servo()

# Control via emotions (high level motions)
s.angry()
time.sleep(2)
s.excited()
time.sleep(2)
s.think()
time.sleep(2)
s.neutral()
time.sleep(2)
s.speak()
time.sleep(2)
s.wiggle_eyes()