#!/usr/local/bin/python3

import requests
import json
import sys

if len(sys.argv) < 3:
    print("usage: create-person.py <sub_key> <person_group> <person_name>")
    sys.exit(1)
# Create PersonGroup:

sub_key=sys.argv[1]
person_group=sys.argv[2]
person_name=sys.argv[3]

url="https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/" + person_group + "/persons"
headers={'Ocp-Apim-Subscription-Key': sub_key, 'Content-Type': 'application/json'}

resp = requests.post(url, headers=headers, data=json.dumps({"name": person_name}))
person_id = json.loads(resp.text)['personId']

print(resp)
print(resp.text)
print("person_id=" + person_id)

with open("face-api/person-group/" + person_group + ".txt", "a") as myfile:
    myfile.write(person_id + " " + person_name + "\n")
