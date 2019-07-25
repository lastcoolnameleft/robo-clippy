#!/usr/local/bin/python3

import requests
import json
import sys

if len(sys.argv) < 3:
    print("usage: add-face.py <sub_key> <person_group> <person_id> <url>")
    sys.exit(1)

sub_key=sys.argv[1]
person_group=sys.argv[2]
person_id=sys.argv[3]
pic_url = sys.argv[4]

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons/" + person_id + "/persistedFaces"
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
resp = requests.post(url, headers=headers, data=json.dumps({"url": pic_url}))
print(resp)
print(resp.text)