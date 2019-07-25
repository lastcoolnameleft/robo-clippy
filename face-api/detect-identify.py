#!/usr/local/bin/python3

import requests
import json
import sys

if len(sys.argv) < 3:
    print("usage: add-face.py <sub_key> <person_group> <url>")
    sys.exit(1)

sub_key=sys.argv[1]
person_group=sys.argv[2]
pic_url = sys.argv[3]

detect_url="https://westus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&recognitionModel=recognition_01&returnRecognitionModel=false&detectionModel=detection_01"
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
resp = requests.post(detect_url, headers=headers, data=json.dumps({"url": pic_url}))
print(resp)
print(resp.text)


identify_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/identify"
faces = [face['faceId'] for face in json.loads(resp.text)]
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

people_dict = {}
f = open('person-group/' + person_group + '.txt', 'r')
for line in f:
    [person_id, name] = line.rstrip().split(' ')
    people_dict[person_id] = name

print("Found " + str(no_of_unknown) + " unknown people")
for person_id in people_id:
    print("Found " + people_dict[person_id])

# take pic
# if no face, do nothing
# If face it recognizes, say "hi tommy"
# if face does not recognize, say "who are you?"
