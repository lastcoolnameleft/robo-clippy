#! /usr/bin/env python3

# -*- coding: utf-8 -*-

###
#Copyright (c) Microsoft Corporation
#All rights reserved. 
#MIT License
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ""Software""), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
import os
import sys
import http.client, urllib.parse, json
from xml.etree import ElementTree
import pyaudio
import wave

from ctypes import *
from contextlib import contextmanager

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)
with noalsaerr():
    p = pyaudio.PyAudio()

# Note: new unified SpeechService API key and issue token uri is per region
# New unified SpeechService key
# Free: https://azure.microsoft.com/en-us/try/cognitive-services/?api=speech-services
# Paid: https://go.microsoft.com/fwlink/?LinkId=872236
api_key = sys.argv[1]
text = sys.argv[2]

params = ""
headers = {"Ocp-Apim-Subscription-Key": api_key}

#AccessTokenUri = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken";
AccessTokenHost = "westus.api.cognitive.microsoft.com"
path = "/sts/v1.0/issueToken"

# Connect to server to get the Access Token
print ("Connect to server to get the Access Token")
conn = http.client.HTTPSConnection(AccessTokenHost)
conn.request("POST", path, params, headers)
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
conn.close()

accesstoken = data.decode("UTF-8")
print ("Access Token: " + accesstoken)

body = ElementTree.Element('speak', version='1.0')
body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
voice = ElementTree.SubElement(body, 'voice')
voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Male')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
voice.text = text # 'This is a demo to call microsoft text to speech service in Python.'

headers = {"Content-type": "application/ssml+xml", 
			"X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
			"Authorization": "Bearer " + accesstoken, 
#			"X-Search-AppId": "07D3234E49CE426DAA29772419F436CA", 
#			"X-Search-ClientID": "1ECFAE91408841A480F00935DC390960", 
			"User-Agent": "TTSForPython"}

from xml.dom import minidom
xmlstr = minidom.parseString(ElementTree.tostring(body)).toprettyxml(indent="   ")
print(xmlstr.encode('utf-8'))

#Connect to server to synthesize the wave
print ("\nConnect to server to synthesize the wave")
conn = http.client.HTTPSConnection("westus.tts.speech.microsoft.com")
#conn.set_debuglevel(5)
conn.request("POST", "/cognitiveservices/v1", ElementTree.tostring(body), headers)
response = conn.getresponse()
print(response.status, response.reason)
wf = wave.open(response)
#p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
CHUNK_SIZE = 1024
data = wf.readframes(CHUNK_SIZE)
print("The synthesized wave length: %d" %(len(data)))
# http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK_SIZE)

conn.close()

# Stop stream.
stream.stop_stream()
stream.close()

# Close PyAudio.
p.terminate()

