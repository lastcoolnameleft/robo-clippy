./clippy-articulation.py
./clippy-speak.py $AZURE_SPEECH_KEY 'hi i am robo clippy'
./clippy-listen.py $LUIS_APP_ID $LUIS_AUTHORING_KEY $AZURE_SPEECH_KEY resources/hey-clippy.pmdl

# S2T
rec -c 1 -r 16000 -b 16 recording.wav
file recording.wav
wget https://raw.githubusercontent.com/Azure-Samples/cognitive-services-speech-sdk/f9807b1079f3a85f07cbb6d762c6b5449d536027/samples/cpp/windows/console/samples/whatstheweatherlike.wav

TOKEN=$(curl -s -X POST "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken" -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" -H "Ocp-Apim-Subscription-Key: $AZURE_SPEECH_KEY")

curl -v -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Accept: application/json" \
    -H "Content-Type: audio/wav; codec=audio/pcm; samplerate=16000" \
    --data-binary @rec.wav \
    "https://westus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US&format=detailed"


# T2S
TOKEN=$(curl -s -X POST -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" -H "Ocp-Apim-Subscription-Key: $AZURE_SPEECH_KEY" "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken")
echo $TOKEN

curl -v -X POST -H "Authorization: Bearer $TOKEN" -H "Accept-Encoding: identity" -H "User-Agent: robo-clippy" -H "Host: westus.tts.speech.microsoft.com" -H "Content-type: application/ssml+xml" -H "X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm" --data '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)">Hello, world!</voice></speak>' "https://westus.tts.speech.microsoft.com/cognitiveservices/v1"
