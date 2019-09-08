. ./env.sh
./clippy-speak.py $AZURE_SPEECH_KEY 'hi i am robo clippy'
./clippy-listen.py $LUIS_APP_ID $LUIS_AUTHORING_KEY $AZURE_SPEECH_KEY $KEYWORD_MODEL $STARTUP_SOUND
./clippy-button-markov.py $AZURE_SPEECH_KEY resources/pickup-lines.txt
./clippy-button-random-line.py $AZURE_SPEECH_KEY resources/compliments.txt
