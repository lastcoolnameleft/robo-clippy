#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import time
import logging
import speech_recognition as sr

from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

# Must be BING Speech Key.  Not Cognitive Services Key
# Holy crap this is stupid.  But I could not find a Python SDK that worked for both T2S and S2T

class SpeechToText(object):

    # This shouldn't change, but might due to other sound devices.
    # import speech_recognition as sr
    # r = sr.Recognizer()
    # sr.Microphone.list_microphone_names()
    DEVICE_INDEX = 2
    recognizer = None
    mic = None

    def __init__(self, luis_app_id, luis_key, bing_speech_key):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        #self.mic = sr.Microphone(device_index=self.DEVICE_INDEX)
        self.luis_app_id = luis_app_id
        self.luis_client = LUISRuntimeClient('https://westus.api.cognitive.microsoft.com',
                                             CognitiveServicesCredentials(luis_key))
        self.bing_speech_key = bing_speech_key

    def get_audio(self):
        logging.debug("get_audio()")
        text = None

        start_time = time.time()
        with self.mic as source:
            logging.debug("get_audio()::going to listen")
            timeout = 3
            audio = self.recognizer.listen(source, timeout)
            logging.debug("get_audio()::Elapsed Time to Listen: %s", str(time.time() - start_time))
        try:
            start_time = time.time()
            text = self.recognizer.recognize_bing(audio, key=self.bing_speech_key)
            logging.debug("get_audio()::Elapsed Time to Bing recognition (s2t): %s", str(time.time() - start_time))
        except sr.UnknownValueError:
            logging.error("Microsoft Bing Voice Recognition could not understand audio")
        except sr.RequestError as exception:
            logging.error("Could not request results from Microsoft Bing Voice Recognition service; %s", exception)
        return text

    def get_intent(self, text):
        if not text:
            return None
        start_time = time.time()
        luis_result = self.luis_client.prediction.resolve(self.luis_app_id, text)
        print("Elapsed Time to LUIS detection: " + str(time.time() - start_time))

        return luis_result

    def get_response(self, intent):
        if not intent:
            return None
        if intent.top_scoring_intent.intent == 'Welcome' and len(intent.entities) > 0:
            return 'I am sorry.  ' + intent.entities[0].entity + ' Is not here'
        else:
            return 'I did not understand you.'
