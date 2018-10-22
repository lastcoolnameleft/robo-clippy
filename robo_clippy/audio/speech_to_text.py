#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import sys
import speech_recognition as sr

from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

# Must be BING Speech Key.  Not Cognitive Services Key
# Holy crap this is stupid.  But I could not find a Python SDK that worked for both T2S and S2T

class Speech_To_Text(object):

    # This shouldn't change, but might due to other sound devices.
    # import speech_recognition as sr
    # r = sr.Recognizer()
    # sr.Microphone.list_microphone_names()
    DEVICE_INDEX = 2
    recognizer = None
    mic = None

    def __init__(self, luis_app_id, luis_key, azure_speech_key, bing_speech_key):
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(device_index=self.DEVICE_INDEX)
        self.luis_app_id = luis_app_id
        self.luis_client = LUISRuntimeClient('https://westus.api.cognitive.microsoft.com',
                                             CognitiveServicesCredentials(luis_key))
        self.bing_speech_key = bing_speech_key

    def get_audio(self):
        text = ''

        with self.mic as source:
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_bing(audio, key=self.bing_speech_key)
        except sr.UnknownValueError:
            print("Microsoft Bing Voice Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
        return text

    def get_intent(self, text):
        if not text:
            return None
        luis_result = self.luis_client.prediction.resolve(self.luis_app_id, text)
        return luis_result

    def get_response(self, intent):
        if not intent:
            return None
        if intent.top_scoring_intent.intent == 'Welcome' and len(intent.entities) > 0:
            return 'I am sorry.  ' + intent.entities[0].entity + ' Is not here'
        else:
            return 'I did not understand you.'
