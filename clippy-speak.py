#!/usr/bin/python3

import sys
import configparser
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo

TEXT = sys.argv[1]
config = configparser.ConfigParser()
config.read('settings.ini')

api_key = config['AZURE']['AZURE_SPEECH_KEY']

s = servo.Servo(config)
a = play.PlayAudio(s)
t2s = text_to_speech.TextToSpeech(api_key)

stream = t2s.get_stream_from_text(TEXT)
a.play_stream(stream)