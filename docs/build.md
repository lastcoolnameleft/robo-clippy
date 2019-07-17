# Build Robo-Clippy

These steps are designed to walk you through building Robo-Clippy

Hardware used:
* https://aiyprojects.withgoogle.com/voice-v1/
* Raspberry Pi 3B+

## Install AIY version of Raspbian

Follow the instructions at https://aiyprojects.withgoogle.com/voice-v1/#assembly-guide

## Install ngrok-notify (optional)

This project will send you a text message when the RaspberryPi reboots.  Not necessary but handy since you might need to reboot a lot.

https://github.com/lastcoolnameleft/ngrok-notify

## Create an Azure Cognitive Services Account

Robo-Clippy uses Azure Cognitive Services for Speech To Text (S2T) and Text To Speech (T2S).  You will need to create the account and store the account keys as environment variables for Robo-Clippy.
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account

## Install Snowboy (Optional)

[Snowboy](https://snowboy.kitt.ai/) is used for keyword detection.  I could not find an easy way to install it, so I compiled from source to get the compiled library and Python module.  Follow instructions here:  https://github.com/kitt-ai/snowboy

*Maybe be out of date, but here's the instructions I followed*:

```
# Make swig
sudo apt-get install libatlas-base-dev libpcre3 libpcre3-dev
wget http://downloads.sourceforge.net/swig/swig-3.0.10.tar.gz
tar xvfz swig-3.0.10.tar.gz 
cd swig-3.0.10
./configure --prefix=/usr --without-clisp --without-maximum-compile-warnings
make
sudo make install
sudo install -v -m755 -d /usr/share/doc/swig-3.0.10
sudo cp -v -R Doc/* /usr/share/doc/swig-3.0.10

# Use swig to install rest of module.  This will be from the cloned repo.
cd swig/Python
make
```

## Install Speech Recognition

The `clippy-listen.py` script uses the popular Python library for hotwork wakeup and S2T:  https://github.com/Uberi/speech_recognition

As of 6/17/19, the pip package has not been updated with the recognize_azure() function.  So, we will need to install from source/master.

```shell
git clone git@github.com:Uberi/speech_recognition.git

pip3 install SpeechRecognition
cd speech_recognition
pip3 install -e .
sudo apt-get install flac
# Verify it's running fine:
python3 -m speech_recognition
```

## Install the Robo-clippy repo

* Follow instructions at: https://github.com/lastcoolnameleft/robo-clippy (You should be here)
* Enable I2C:
    * `sudo raspi-config`
    * Select "Interfacing Options" -> "I2C" -> Yes to Enable
```shell
git@github.com:lastcoolnameleft/robo-clippy.git
cd robo-clippy
pip3 install -r requirements.txt
cp env.sh.template env.sh
# Modify env.sh to add the environment variable values
. ./env.sh
```