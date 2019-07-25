#!/usr/local/bin/python3

import requests
import json
import sys

if len(sys.argv) < 3:
    print("usage: train-status.py <sub_key> <person_group>")
    sys.exit(1)

sub_key=sys.argv[1]
person_group=sys.argv[2]

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/training"
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
resp = requests.get(url, headers=headers)
print(resp)
print(resp.text)
