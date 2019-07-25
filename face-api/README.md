Examples:

# Create and train
```
PERSON_GROUP=test9
python3 face-api/create-person-group.py $FACE_API_KEY $PERSON_GROUP
touch face-api/person-group/$PERSON_GROUP.txt 

PERSON=shiva
python3 face-api/create-person.py $FACE_API_KEY $PERSON_GROUP $PERSON
PERSON_ID=$(tail -1 face-api/person-group/$PERSON_GROUP.txt | awk '{print $1}')
python3 face-api/add-face-multiple.py $FACE_API_KEY $PERSON_GROUP $PERSON_ID face-api/$PERSON.txt

PERSON=tommy
python3 create-person.py $FACE_API_KEY $PERSON_GROUP $PERSON
PERSON_ID=$(tail -1 person-group/$PERSON_GROUP.txt | awk '{print $1}')
python3 add-face-multiple.py $FACE_API_KEY $PERSON_GROUP $PERSON_ID $PERSON.txt

# Train
python3 face-api/train.py $FACE_API_KEY $PERSON_GROUP
python3 face-api/train-status.py $FACE_API_KEY $PERSON_GROUP


```

# Delete Person Group

```
python3 face-api/delete-person-group.py $FACE_API_KEY $PERSON_GROUP
```

# old stuff

```
python3 add-face.py $FACE_API_KEY $PERSON_GROUP $PERSON_ID "http://www.lastcoolnameleft.com/mini/pics/me1.png"

```

# examples:
Pic of TommY: https://live.staticflickr.com/4527/24086902877_56807acc88_d.jpg