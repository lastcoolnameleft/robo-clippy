# Robo Clippy

This repository contains the details for the inspiration, build, and design of Robo-Clippy

Click to watch the video.
[![Watch the video](https://img.youtube.com/vi/vIm4QBJv_Rk/maxresdefault.jpg
)](https://twitter.com/lastcoolname/status/1141912071820517376)

## Background

I love LEGO and never stopped building.  My position as a Cloud Solution Architect for Microsoft has helped me do this in the real world as well as in the virtual world.  It's a dream come true.  

View the presentation
[![View the presentation](https://raw.githubusercontent.com/lastcoolnameleft/robo-clippy/master/docs/assets/robo-clippy-presentation.jpg)](https://speakerdeck.com/lastcoolnameleft/roboclippy)

I was inspired by the [Big Mouth Billy Bass Alexa hack](https://www.youtube.com/watch?v=aW5TvT1mo9k) and wanted to build something similar, but with more passion.  Like or love, there's no denying that people have strong feelings about Clippy.

## Technologies used

The Big Mouth Billy Back Alexa hack was very neat, but simple.  It used an Arduino to move the mouth when audio was present.  This solution directly incorporates multiple technologies across the board into one package.

* [Azure Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech/) - For Text to Speech (T2S) and Speech to Text (S2T)
* [LUIS](https://www.luis.ai/home) - Used for Natural Language Processing (NLP)
* [Snowboy](https://snowboy.kitt.ai/) - for hotword/keyword wakeup
* [I2C](https://github.com/adafruit/Adafruit_Python_PCA9685) - for Servo Controls
  * https://www.amazon.com/gp/product/B014KTSMLA/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1
  * https://www.youtube.com/watch?v=Rp6VvvjSGSs
* [Google AIY Voice Kit](https://aiyprojects.withgoogle.com/voice/) - Yes, I know it's from Google, but why should that stop me from using the right tool for the job?  It incorporates a nicely integrated Microphone and Speaker system.

## Usage

If you are interested in building your own, I have [detailed install instructions](https://github.com/lastcoolnameleft/robo-clippy/blob/master/docs/build.md) along with [troubleshooting details](https://github.com/lastcoolnameleft/robo-clippy/blob/master/docs/debug.md) and [examples](https://github.com/lastcoolnameleft/robo-clippy/blob/master/docs/run.md).

## Vision

If you are interested in seeing the results from the 2019 Microsoft Hackathon, [see the hackathon branch](https://github.com/lastcoolnameleft/robo-clippy/blob/hackathon/face-api/README.md).
