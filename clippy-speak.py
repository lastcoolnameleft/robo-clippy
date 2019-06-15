#!/usr/bin/python3

import sys
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo

api_key = sys.argv[1]
text = sys.argv[2]

s = servo.Servo()
a = play.PlayAudio(s)
t2s = text_to_speech.TextToSpeech(api_key)

stream = t2s.get_stream_from_text(text)
a.play_stream(stream)