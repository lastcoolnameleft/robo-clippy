#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import os
import time
import logging
import signal
import pprint
import requests

import speech_recognition as sr
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

class SpeechToText(object):

    # This shouldn't change, but might due to other sound devices.
    # import speech_recognition as sr
    # r = sr.Recognizer()
    # sr.Microphone.list_microphone_names()
    DEVICE_INDEX = 2
    recognizer = None
    mic = None
    servo = None

    def __init__(self, servo, luis_app_id, luis_key, azure_speech_key):
        self.servo = servo
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        #self.mic = sr.Microphone(device_index=self.DEVICE_INDEX)
        self.luis_app_id = luis_app_id
        self.luis_client = LUISRuntimeClient('https://westus.api.cognitive.microsoft.com',
                                             CognitiveServicesCredentials(luis_key))
        self.azure_speech_key = azure_speech_key

    def get_audio(self):
        logging.info("get_audio()")
        text = None
        start_time = time.time()
        with self.mic as source:
            timeout = 3
            audio = self.recognizer.listen(source, timeout)
            logging.debug("get_audio()::Elapsed Time to Listen: %s", str(time.time() - start_time))
        try:
            text = self.recognizer.recognize_azure(audio, key=self.azure_speech_key)
            start_time = time.time()
            logging.debug("get_audio()::Elapsed Time to Azure Speech recognition (s2t): %s", str(time.time() - start_time))
        except sr.UnknownValueError:
            logging.error("Microsoft Azure Speech Recognition could not understand audio")
        except sr.RequestError as exception:
            logging.error("Could not request results from Microsoft Azure Speech Recognition service; %s", exception)
        logging.debug("Utterance = %s", text)
        return text

    def get_intent(self, text):
        if not text:
            return None
        start_time = time.time()
        luis_result = self.luis_client.prediction.resolve(self.luis_app_id, text)
        print("Elapsed Time to LUIS detection: " + str(time.time() - start_time))
        return luis_result

    def get_response(self, intent):
        top_scoring_intent = intent.top_scoring_intent.intent
        logging.info("intent = %s", top_scoring_intent)
        if not intent:
            return None
        if top_scoring_intent == 'Welcome' and len(intent.entities) > 0:
            return 'I am sorry.  ' + intent.entities[0].entity + ' Is not here'
        elif top_scoring_intent == 'How many':
            return intent.entities[0].entity + ' has 2 ' + intent.entities[1].entity
        elif top_scoring_intent == 'Is Awesome':
            return 'I think ' + intent.entities[0].entity + ' is awesome'
        elif top_scoring_intent == 'lanyard':
            action = intent.entities[0].entity
            self.lanyard_request(action)
            return ''
        elif top_scoring_intent == 'Show Me':
            entity = intent.entities[0].entity
            print('entity=' + entity)
            if entity == 'angry':
                self.servo.angry()
                self.servo.mouth_neutral()
            elif entity == 'excited':
                self.servo.excited()
                self.servo.mouth_forward_full()
            elif entity == 'neutral':
                self.servo.neutral()
                self.servo.mouth_neutral()
            return None
        else:
            return 'I did not understand you.'

    def lanyard_request(self, action):
        url = ' https://lanyard-api.ngrok.io/lanyard'
        r = requests.post(url, data={'setting': action})