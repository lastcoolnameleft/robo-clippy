# Run Robo-clippy

* `clippy-speak.py` - Invokes T2S and moves Robo-Clippy's mouth
* `clippy-listen.py` - Uses T2S + S2T + LUIS to have an interactive session

# Get Clippy to say something and articulate

```shell
./clippy-speak.py $AZURE_SPEECH_KEY 'hi i am robo clippy'
```

# Use Speaker and Microphone to interact with Clippy + arcticulate

```shell
./clippy-listen.py $LUIS_APP_ID $LUIS_AUTHORING_KEY $AZURE_SPEECH_KEY resources/hey-clippy.pmdl
```