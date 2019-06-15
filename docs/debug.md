# Debugging

## Common issues:

* `OSError: [Errno 121] Remote I/O error` - This is due to Python being unable to speak to the PCA9685 board.  Check your connections.
* Sometimes the servos will make grinding noises.   This can happen when it wants to move to a specific position, but is blocked.  Check if anything is pushing against servo arm.

## Audio

Various tools for debugging the audio

Good tutorial:  http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/

```
# Play pink noise
speaker-test

# Play audio clip
aplay /usr/share/sounds/alsa/Front_Center.wav

# See all audio devices
aplay -L

# ASCII GUI 
alsamixer
```

## Speech 2 Text

Use this to verify Azure T2S is working properly

The commands do the following:

* Record audio from Microphone.  Save to /tmp/recording.wav
* Using Azure Speech Key, get Auth Token
* Upload Wav file

```shell
# Record a Wav file from microphone.  Hit Control-C when done.
rec -c 1 -r 16000 -b 16 /tmp/recording.wav
file /tmp/recording.wav
# Should see: /tmp/recording.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 16000 Hz

# If you don't want to create a recording, can use existing file
wget https://raw.githubusercontent.com/Azure-Samples/cognitive-services-speech-sdk/f9807b1079f3a85f07cbb6d762c6b5449d536027/samples/cpp/windows/console/samples/whatstheweatherlike.wav

# Get token from Cognitive Services API
TOKEN=$(curl -s -X POST "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken" -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" -H "Ocp-Apim-Subscription-Key: $AZURE_SPEECH_KEY")

# Submit WAV to Cognitive Services to get the text spoken
curl -v -X POST \
    -H "Authorization: Bearer $TOKEN" \
    -H "Accept: application/json" \
    -H "Content-Type: audio/wav; codec=audio/pcm; samplerate=16000" \
    --data-binary @/tmp/recording.wav \
    "https://westus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US&format=detailed"
```

## Text 2 Speech

Use this to verify Azure T2S is working properly.  

The commands do the following:

* Using Azure Speech Key, get Auth Token
* Using Auth Token, get wav format from Azure Cognitive Services.  Save to file
* Play file

```shell
#Get a token from the Cognitive Services API
TOKEN=$(curl -s -X POST -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" -H "Ocp-Apim-Subscription-Key: $AZURE_SPEECH_KEY" "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken")
echo $TOKEN

# Using that token get a WAV file
curl -v -X POST -H "Authorization: Bearer $TOKEN" -H "Accept-Encoding: identity" -H "User-Agent: robo-clippy" -H "Host: westus.tts.speech.microsoft.com" -H "Content-type: application/ssml+xml" -H "X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm" --data '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)">Hello, world!</voice></speak>' "https://westus.tts.speech.microsoft.com/cognitiveservices/v1" > /tmp/t2s.wav
aplay /tmp/t2s.wav
```