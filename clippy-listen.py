#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import sys
import logging

from robo_clippy.audio import speech_to_text, text_to_speech, play

# Must be BING Speech Key.  Not Cognitive Services Key
# Holy crap this is stupid.  But I could not find a Python SDK that worked for both T2S and S2T
LUIS_APP_ID = sys.argv[1]
LUIS_AUTHORING_KEY = sys.argv[2]
AZURE_SPEECH_KEY = sys.argv[3]
BING_SPEECH_API_KEY = sys.argv[4]

def main():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    logging.StreamHandler(sys.stdout)

    s2t = speech_to_text.SpeechToText(LUIS_APP_ID, LUIS_AUTHORING_KEY, BING_SPEECH_API_KEY)
    t2s = text_to_speech.Text_to_Speech(AZURE_SPEECH_KEY)
    audio = play.PlayAudio()

    while True:
        #input('press enter when ready to listen')
        logging.debug('starting to listen')
        text = s2t.get_audio()
        if not text:
            continue
        logging.debug('recognized text = %s', text)
        intent = s2t.get_intent(text)
        response = s2t.get_response(intent)
        logging.debug('response = %s', response)
        stream = t2s.get_stream_from_text(response)
        logging.debug('playing stream')
        audio.play_stream(stream)

main()
