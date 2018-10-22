#!/usr/bin/python3

import sys
from robo_clippy.audio import play, text_to_speech

api_key = sys.argv[1]
text = sys.argv[2]

a = play.PlayAudio()
t2s = text_to_speech.Text_to_Speech(api_key)

stream = t2s.get_stream_from_text(text)
a.play_stream(stream)