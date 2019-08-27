#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import os
import sys
import logging

from robo_clippy import servo
from robo_clippy.audio import speech_to_text, text_to_speech, play, snowboydecoder
from aiy.board import Board, Led

# Must be BING Speech Key.  Not Cognitive Services Key
# Holy crap this is stupid.  But I could not find a Python SDK that worked for both T2S and S2T
LUIS_APP_ID = sys.argv[1]
LUIS_AUTHORING_KEY = sys.argv[2]
AZURE_SPEECH_KEY = sys.argv[3]
KEYWORD_MODEL = sys.argv[4]
STARTUP_SOUND = sys.argv[5]

board = Board()
board.led.state = Led.OFF
servo = servo.Servo()
audio = play.PlayAudio(servo)
s2t = speech_to_text.SpeechToText(servo, LUIS_APP_ID, LUIS_AUTHORING_KEY, AZURE_SPEECH_KEY)
t2s = text_to_speech.TextToSpeech(AZURE_SPEECH_KEY)

def main():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    logging.StreamHandler(sys.stdout)
    audio.play_file(STARTUP_SOUND)

    detector = snowboydecoder.HotwordDetector(KEYWORD_MODEL, sensitivity=0.38)
    detector.start(detected_callback=listen_and_process, sleep_time=0.03)

def listen_and_process():
    board.led.state = Led.PULSE_QUICK
    #board.led.state = Led.ON
    servo.think()
    text = s2t.get_audio()
    if not text:
        board.led.state = Led.OFF
        return
    logging.debug('recognized text = %s', text)
    intent = s2t.get_intent(text)
    response = s2t.get_response(intent)
    logging.debug('response = %s', response)
    if response:
        stream = t2s.get_stream_from_text(response)
        board.led.state = Led.OFF
        logging.debug('playing stream')
        audio.play_stream(stream)
    else:
        board.led.state = Led.OFF


main()
