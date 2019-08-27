#!/usr/bin/python3 -u
import logging
import platform
import sys
import markovify
import sys
import random
import time
from robo_clippy.audio import play, text_to_speech
from robo_clippy import servo
from aiy.board import Board, Led

api_key = sys.argv[1]
text_file = sys.argv[2]
shutdown_sound = sys.argv[3]
lines = open(text_file).read().splitlines()

servo = servo.Servo()
audio = play.PlayAudio(servo)
t2s = text_to_speech.TextToSpeech(api_key)
board = Board()
last_time_pressed = time.time()

def on_button_pressed():
    global last_time_pressed
    last_time_pressed = time.time()
    print('on_button_pressed()')
    board.led.state = Led.ON
    text = random.choice(lines)
    print(text)
    stream = t2s.get_stream_from_text(text)
    audio.play_stream(stream)
    board.led.state = Led.OFF

def on_button_release():
    global last_time_pressed
    now = time.time()
    elapsed_button_time = now - last_time_pressed
    last_time_pressed = now
    print('on_button_release()::' + str(elapsed_button_time))
    if elapsed_button_time > 3:
        print('GOING TO REBOOT')
        restart()

def restart():
    global shutdown_sound
    print('RESTART!')
    audio.play_file(shutdown_sound)
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

last_time_pressed = time.time()
board.button.when_pressed = on_button_pressed
board.button.when_released = on_button_release
print('READY')