#!/usr/bin/python3

import sys
from robo_clippy import audio, text2speech

api_key = sys.argv[1]
text = sys.argv[2]

a = audio.play.PlayAudio()
t2s = text2speech.Text2Speech(api_key)

stream = t2s.get_stream_from_text(text)
a.play_stream(stream)