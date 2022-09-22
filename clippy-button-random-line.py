#!/usr/bin/python3 -u
import sys
import random
import time
import configparser
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo
from aiy.board import Board, Led

config = configparser.ConfigParser()
config.read('settings.ini')

api_key = config['AZURE']['AZURE_SPEECH_KEY']
shutdown_sound = config['MISC']['SHUTDOWN_SOUND']

text_file = sys.argv[1]
lines = open(text_file).read().splitlines()

servo = servo.Servo(config)
audio = play.PlayAudio(servo)
t2s = text_to_speech.TextToSpeech(api_key)
board = Board()
LAST_TIME_PRESSED = time.time()

def on_button_pressed():
    global LAST_TIME_PRESSED
    LAST_TIME_PRESSED = time.time()
    print('on_button_pressed()')
    board.led.state = Led.ON
    text = random.choice(lines)
    print(text)
    stream = t2s.get_stream_from_text(text)
    audio.play_stream(stream)
    board.led.state = Led.OFF

def on_button_release():
    global LAST_TIME_PRESSED
    now = time.time()
    elapsed_button_time = now - LAST_TIME_PRESSED
    LAST_TIME_PRESSED = now
    print('on_button_release()::' + str(elapsed_button_time))

LAST_TIME_PRESSED = time.time()
board.button.when_pressed = on_button_pressed
board.button.when_released = on_button_release
print('READY')