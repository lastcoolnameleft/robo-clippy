#!/usr/bin/python3

import requests
import json
import sys
import os
import time
from robo_clippy.audio import play, text_to_speech, speech_to_text
from robo_clippy import servo
from datetime import datetime
from azure.storage.blob import BlockBlobService, PublicAccess

if len(sys.argv) < 3:
    print("usage: clippy-face-api.py <sub_key> <azure speech api key> <person_group>")
    sys.exit(1)

sub_key=sys.argv[1]
speech_api_key=sys.argv[2]
blob_account_name=sys.argv[3]
blob_account_key=sys.argv[4]
luis_app_id=sys.argv[5]
luis_authoring_key=sys.argv[6]
person_group=sys.argv[7]

s = servo.Servo()
a = play.PlayAudio(s)
t2s = text_to_speech.TextToSpeech(speech_api_key)
s2t = speech_to_text.SpeechToText(servo, luis_app_id, luis_authoring_key, speech_api_key)
block_blob_service = BlockBlobService(account_name=blob_account_name, account_key=blob_account_key)

def take_and_upload_picture():
    container_name = 'clippy'
    now = datetime.now()
    image_file = "image-" + now.strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"
    image_path = '/tmp/' + image_file
    command = 'fswebcam ' + image_path
    print("going to run: " + command)
    os.system(command)
    res = block_blob_service.create_blob_from_path(container_name, image_file, image_path)
    print("res = " + (str(res)))
    # Example: https://shivaiotsensordata.blob.core.windows.net/clippy/image.jpg
    image_url = 'https://' + blob_account_name + '.blob.core.windows.net/clippy/' + image_file
    print(image_url)
    return image_url

def get_faces(sub_key, person_group, pic_url):
    detect_url="https://westus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&recognitionModel=recognition_01&returnRecognitionModel=false&detectionModel=detection_01"
    headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
    resp = requests.post(detect_url, headers=headers, data=json.dumps({"url": pic_url}))
    print(resp)
    print(resp.text)
    faces = [face['faceId'] for face in json.loads(resp.text)]
    return faces

def get_people_dict(person_group):
    people_dict = {}
    f = open('face-api/person-group/' + person_group + '.txt', 'r')
    for line in f:
        [person_id, name] = line.rstrip().split(' ')
        people_dict[person_id] = name
    return people_dict

def identify_faces(sub_key, person_group, faces):
    identify_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/identify"
    headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
    body = {
        "personGroupId": person_group,
        "faceIds": faces,
        "maxNumOfCandidatesReturned": 1,
        "confidenceThreshold": 0.5
    }
    print(body)
    resp = requests.post(identify_url, headers=headers, data=json.dumps(body))
    response = json.loads(resp.text)
    print(resp)
    print(response)
    people_id = [person['candidates'][0]['personId'] for person in response if person['candidates']]
    no_of_unknown = len([person['candidates'] for person in response if not person['candidates']])


    return people_id, no_of_unknown

def speak(text):
    print("CLIPPY SAYS: " + speech_to_say)
    stream = t2s.get_stream_from_text(text)
    a.play_stream(stream)

def listen():
    text = s2t.get_audio()
    if not text:
        return
    print('recognized text = %s', text)
    return text

def add_person_with_pics(person_group, person_name, pic_list):
    #time.sleep(10)
    url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons"
    headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}

    # Add person to person group
    resp = requests.post(url, headers=headers, data=json.dumps({"name": person_name}))
    person_id = json.loads(resp.text)['personId']

    print(resp)
    print(resp.text)
    print("person_id=" + person_id)

    with open("face-api/person-group/" + person_group + ".txt", "a") as myfile:
        myfile.write(person_id + " " + person_name + "\n")

    # Add snapshots taken
    for pic_url in pic_list:
        print("\n\nProcessing " + pic_url)
        url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons/" + person_id + "/persistedFaces"
        headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
        resp = requests.post(url, headers=headers, data=json.dumps({"url": pic_url}))
        print(resp)
        print(resp.text)

    # Retrain
    url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/train"
    headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
    resp = requests.post(url, headers=headers, data=json.dumps({}))
    print(resp)
    print(resp.text)

# take pic.  Get faces
# if no face, do nothing
# if faces, try to recognize faces.
    # If face it recognizes, say "hi tommy"
    # if face does not recognize, say "who are you?"
pic_url = take_and_upload_picture()
faces = get_faces(sub_key, person_group, pic_url)


if len(faces) == 0:
    print("CLIPPY: Do nothing")
    exit(0)
#print("faces = " + str(faces))
[known_people, no_of_unknown] = identify_faces(sub_key, person_group, faces)

people_dict = get_people_dict(person_group)
print("Found " + str(no_of_unknown) + " unknown people")
for person_id in known_people:
    print("Found " + people_dict[person_id])

if len(known_people) > 0:
    speech_to_say = "hi " + people_dict[known_people[0]]
    speak(speech_to_say)
else:
    stranger_image_1 = take_and_upload_picture()
    speech_to_say = "Hi! I don't think we've met! I'm Clippy! What's YOUR name?"
    speak(speech_to_say)
    name = listen()
    #name = 'jenny'
    print("CLIPPY HEARD: " + name)
    stranger_image_2 = take_and_upload_picture()
    speak("Thanks.  I hope I can remember that.")
    stranger_image_3 = take_and_upload_picture()
    add_person_with_pics(person_group, name, [stranger_image_1, stranger_image_2, stranger_image_3])