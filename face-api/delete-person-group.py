#!/usr/local/bin/python3

import requests
import json
import sys

if len(sys.argv) < 3:
    print("usage: create-person-group.py <sub_key> <person_group>")
    sys.exit(1)
# Create PersonGroup:

sub_key=sys.argv[1]
person_group=sys.argv[2]

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}
resp = requests.delete(url, headers=headers)
print(resp)
print(resp.text)