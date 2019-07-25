. ./env.sh
./clippy-speak.py $AZURE_SPEECH_KEY 'hi i am robo clippy'
./clippy-listen.py $LUIS_APP_ID $LUIS_AUTHORING_KEY $AZURE_SPEECH_KEY resources/hey-clippy.pmdl

./clippy-iot.py $CONNECTION_STRING $QUEUE_NAME $AZURE_SPEECH_KEY
./clippy-clear-queue.py $CONNECTION_STRING $QUEUE_NAME


# Face API Example
PERSON_GROUP=test
python3 face-api/create-person-group.py $FACE_API_KEY $PERSON_GROUP
touch face-api/person-group/$PERSON_GROUP.txt

PERSON=shiva
python3 face-api/create-person.py $FACE_API_KEY $PERSON_GROUP $PERSON
PERSON_ID=$(tail -1 face-api/person-group/$PERSON_GROUP.txt | awk '{print $1}')
python3 face-api/add-face-multiple.py $FACE_API_KEY $PERSON_GROUP $PERSON_ID face-api/$PERSON.txt

# Train
python3 face-api/train.py $FACE_API_KEY $PERSON_GROUP
python3 face-api/train-status.py $FACE_API_KEY $PERSON_GROUP

face-api/clippy-face-api.py $FACE_API_KEY $AZURE_SPEECH_KEY $BLOB_ACCOUNT_NAME $BLOB_ACCOUNT_KEY $LUIS_APP_ID $LUIS_AUTHORING_KEY $PERSON_GROUP
