#!/usr/bin/python3

import logging
import platform
import sys
import markovify
import sys
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo
from aiy.board import Board, Led

api_key = sys.argv[1]
text_file = sys.argv[2]

with open(text_file) as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)
servo = servo.Servo()
audio = play.PlayAudio(servo)
t2s = text_to_speech.TextToSpeech(api_key)
board = Board()

def on_button_pressed():
    # Check if we can start a conversation. 'self._can_start_conversation'
    # is False when either:
    # 1. The assistant library is not yet ready; OR
    # 2. The assistant library is already in a conversation.
    text = text_model.make_sentence()
    print(text)
    stream = t2s.get_stream_from_text(text)
    audio.play_stream(stream)

board.button.when_pressed = on_button_pressed
print('READY')