#!/usr/bin/python3 -u
import logging
import platform
import sys
import markovify
import sys
import random
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo
from aiy.board import Board, Led

api_key = sys.argv[1]
text_file = sys.argv[2]
lines = open(text_file).read().splitlines()

servo = servo.Servo()
audio = play.PlayAudio(servo)
t2s = text_to_speech.TextToSpeech(api_key)
board = Board()

def on_button_pressed():
    board.led.state = Led.ON
    text = random.choice(lines)
    print(text)
    stream = t2s.get_stream_from_text(text)
    audio.play_stream(stream)
    board.led.state = Led.OFF

board.button.when_pressed = on_button_pressed
print('READY')