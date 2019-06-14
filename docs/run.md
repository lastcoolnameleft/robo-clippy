# Run Robo-clippy

There are 3 major scripts.

* `clippy-articulation.py` - Moves the servos when audio is detected
* `clippy-speak.py` - Invokes T2S
* `clippy-listen.py` - Uses T2S + S2T + LUIS to have an interactive session

# Get Clippy to say something and articulate

```shell
# In Window #1
clippy-articulation.py
# In Window #2
./clippy-speak.py $AZURE_SPEECH_KEY 'hi i am robo clippy'
```

# Use Speaker and Microphone to interact with Clippy + arcticulate

```shell
# In Window #1
clippy-articulation.py
# In Window #2
./clippy-listen.py $LUIS_APP_ID $LUIS_AUTHORING_KEY $AZURE_SPEECH_KEY resources/hey-clippy.pmdl
```