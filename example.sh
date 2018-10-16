KEY=$(az cognitiveservices account keys list -g clippy -n clippy-speech -o json | jq '.key1' -r)
echo $KEY

python3 clippy-conversation.py $KEY 'hi i am robo clippy'

TOKEN=$(curl -s -X POST -H "Content-type: application/x-www-form-urlencoded" -H "Content-Length: 0" -H "Ocp-Apim-Subscription-Key: $KEY" "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken")
echo $TOKEN

curl -v -X POST -H "Authorization: Bearer $TOKEN" -H "Accept-Encoding: identity" -H "User-Agent: robo-clippy" -H "Host: westus.tts.speech.microsoft.com" -H "Content-type: application/ssml+xml" -H "X-Microsoft-OutputFormat: riff-24khz-16bit-mono-pcm" --data '<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)">Hello, world!</voice></speak>' "https://westus.tts.speech.microsoft.com/cognitiveservices/v1"
