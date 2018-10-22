#!/usr/bin/python3

# Inspired by https://realpython.com/python-speech-recognition/#working-with-microphones
# https://github.com/Uberi/speech_recognition#readme

import sys
import speech_recognition as sr

from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

from robo_clippy import audio, text2speech

# Must be BING Speech Key.  Not Cognitive Services Key
# Holy crap this is stupid.  But I could not find a Python SDK that worked for both T2S and S2T
BING_SPEECH_API_KEY = sys.argv[1]
AZURE_SPEECH_KEY = sys.argv[2]
LUIS_APP_ID = sys.argv[3]
LUIS_AUTHORING_KEY = sys.argv[4]
DEVICE_INDEX = 2

def get_mic(device_index):
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=device_index)
    return mic, r

def get_audio(mic, recognizer, api_key):
    text = ''

    with mic as source:
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_bing(audio, key=api_key)
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
    return text

def get_intent(text, app_id, authoring_key):
    if not text:
        return None
    client = LUISRuntimeClient('https://westus.api.cognitive.microsoft.com',
                               CognitiveServicesCredentials(authoring_key))
    luis_result = client.prediction.resolve(app_id, text)
    return luis_result

def get_response(intent):
    if not intent:
        return None
    if intent.top_scoring_intent.intent == 'Welcome' and len(intent.entities) > 0:
        return 'I am sorry.  ' + intent.entities[0].entity + ' Is not here'
    else:
        return 'I did not understand you.'

def speak(text, api_key):
    if not text:
        return None
    a = audio.play.PlayAudio()
    t2s = text2speech.Text2Speech(api_key)

    stream = t2s.get_stream_from_text(text)
    a.play_stream(stream)

mic, recognizer = get_mic(DEVICE_INDEX)
input('press enter when ready')
text = get_audio(mic, recognizer, BING_SPEECH_API_KEY)
intent = get_intent(text, LUIS_APP_ID, LUIS_AUTHORING_KEY)
response = get_response(intent)
speak(response, AZURE_SPEECH_KEY)