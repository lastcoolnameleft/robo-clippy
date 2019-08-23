import time
import sys
import logging
import http.client, urllib.parse, json
from xml.etree import ElementTree
from xml.dom import minidom

class TextToSpeech(object):

    api_key = None
    def __init__(self, api_key):
        self.api_key = api_key

    def get_access_token(self):
        params = ""
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        access_token_host = "westus.api.cognitive.microsoft.com"
        path = "/sts/v1.0/issueToken"

        # Connect to server to get the Access Token
        logging.debug("Connect to server to get the Access Token")
        conn = http.client.HTTPSConnection(access_token_host)
        conn.request("POST", path, params, headers)
        response = conn.getresponse()
        logging.debug(response.status, response.reason)

        data = response.read()
        conn.close()

        accesstoken = data.decode("UTF-8")
        #print ("Access Token: " + accesstoken)
        return accesstoken

    def get_stream_from_text(self, text):
        start_time = time.time()
        access_token = self.get_access_token()
        body = ElementTree.Element('speak', version='1.0')
        body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
        voice = ElementTree.SubElement(body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
        voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Male')
        voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
        voice.text = text

        headers = {"Content-type": "application/ssml+xml", 
                   "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
                   "Authorization": "Bearer " + access_token,
                   "User-Agent": "Robo-Clippy"}

        xmlstr = minidom.parseString(ElementTree.tostring(body)).toprettyxml(indent="   ")
        logging.info(xmlstr.encode('utf-8'))

        #Connect to server to synthesize the wave
        logging.debug("Connect to server to synthesize the wave")
        conn = http.client.HTTPSConnection("westus.tts.speech.microsoft.com")
        #conn.set_debuglevel(5)
        conn.request("POST", "/cognitiveservices/v1", ElementTree.tostring(body), headers)
        response = conn.getresponse()
        logging.debug(response.status, response.reason)
        logging.debug("Elapsed Time to Bing recognition (t2s): " + str(time.time() - start_time))
        #conn.close()
        return response
