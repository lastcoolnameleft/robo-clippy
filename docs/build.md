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