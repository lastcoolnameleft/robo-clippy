sub_key=""
person_group="test2"

import requests
import json
import sys

if len(sys.argv) < 1:
    print("usage: face-api-train.py <sub_key> <person_group> <person_name> <url>")
    sys.exit(1)
# Create PersonGroup:

sub_key=sys.argv[1]
person_group=sys.argv[2]
person_name=sys.argv[3]
url=sys.argv[4]

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group
body={'name': person_group}
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
resp = requests.put(url, data=json.dumps(body), headers=headers)
resp
resp.text

# Create PersonGroup Person

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons"
person_name="tommy"

resp = requests.post(url, headers=headers, data=json.dumps({"name": person_name}))
resp
resp.text
personId = json.loads(resp.text)['personId']

# Add Face

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons/" + personId + "/persistedFaces"
pic_url="http://www.lastcoolnameleft.com/mini/pics/me1.png"
resp = requests.post(url, headers=headers, data=json.dumps({"url": pic_url}))
resp
resp.text
persistedFaceId = json.loads(resp.text)['persistedFaceId']

# Train

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/train"
resp = requests.post(url, headers=headers, data=json.dumps({}))
resp
resp.text
