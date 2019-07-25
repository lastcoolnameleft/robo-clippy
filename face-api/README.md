# Face API Hackathon

In the 2019 Microsoft Hackathon, a team of 5 computer and social scientists joined together to imbue Robo-Clippy with Vision with the goal to recognize faces and train on new ones.

# Lessons learned

We explored 3 different hardware technologies for detecting people from their face:

* [https://azure.github.io/Vision-AI-DevKit-Pages](Azure Vision AI DevKit): This kit has the potential to bundle all of our requirements into one solution.  However, due to congested WiFi and other limitations (would not add message to IotHub when face was detected, but not identified), we were not able to use this for our project.
* [OpenCV](https://opencv.org/):  We were able to get this to work on the RaspberryPi; however, only with Python2.  Given all of the code was written with Python3 and we didn't want to go back, this was a significant blocker.
* USB WebCam: This solution required writing a lot of the code ourselves, but was functional. (But was not without problems:  [USB Camera required a reset of the USB plug every few pics taken](https://www.raspberrypi.org/forums/viewtopic.php?t=86265))

With all of this in mind, we used the USB Webcam going forward in the hack.  The logical flow is as follows:

## Train with a single Face

* Use the Face API to create a Person Group.  This is the collection/sandbox for storing pics and people.
* Use the Face API to create a Person.  The API would input a name (e.g. Tommy) and return a GUID.  This GUID needs to be stored in your own system
* Use the Face API to upload training pictures.
* Train the Face API
* Check when training was complete.  (with 10 photos, this was almost instant)

## Start with RoboClippy

* RoboClippy will use the USB Webcam to take a photo, save the image and then upload it to Azure Blob Storage account.
* Use the "Detect Face" API to find faces in the photo.  (we only used one face at a time)
* Use the "Identify Face" API to return the list of GUIDs (see steps above) to get the Person in the photo
* Lookup in a text file which name (e.g. Tommy) corresponds to the GUID
* If no identified faces are found, ask for the name ("I don't think we've met") and then train on that face (see above steps)
* If an identified face is found, say "Hi $person_name"

## Code

To get and get started, a script functionality (e.g. create person group, create person, train, etc.) was created and added to the face-api folder in this repo.

* create-person-group.py:  Creates the Person Group.  This must be done first.
* create-person.py:  This must be done for each person.  Returns a GUID
* add-face-multiple.py:  Expects a Person GUID and a file with a list of URL's for that person to ingest
* train: Tells Face API to start training on those people
* train-status.py:  Returns the status of the progress of the training

# Create and train
```
# Create the Person Group
PERSON_GROUP=test9
python3 face-api/create-person-group.py $FACE_API_KEY $PERSON_GROUP
touch face-api/person-group/$PERSON_GROUP.txt 

# Create a person and upload the images to be trained
PERSON=shiva
python3 face-api/create-person.py $FACE_API_KEY $PERSON_GROUP $PERSON
PERSON_ID=$(tail -1 face-api/person-group/$PERSON_GROUP.txt | awk '{print $1}')
python3 face-api/add-face-multiple.py $FACE_API_KEY $PERSON_GROUP $PERSON_ID face-api/$PERSON.txt

# Traina using the faces uploaded
python3 face-api/train.py $FACE_API_KEY $PERSON_GROUP
python3 face-api/train-status.py $FACE_API_KEY $PERSON_GROUP
```

## Cleanup

To delete a Person Group (and all people and faces):

```
python3 face-api/delete-person-group.py $FACE_API_KEY $PERSON_GROUP
```
