# pylint: disable=E0401
# Disabling because OSX can't install alsaaudio

# Inspired by https://stackoverflow.com/questions/1936828/how-get-sound-input-from-microphone-in-python-and-process-it-on-the-fly
## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio
import audioop
import logging
from struct import unpack
import numpy as np

class DetectAudio(object):

    inp = None

    def __init__(self):
        logging.info("starting up")
        # Open the device in nonblocking capture mode. The last argument could
        # just as well have been zero for blocking mode. Then we could have
        # left out the sleep call in the bottom of the loop
        self.inp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device='default')

        # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
        self.inp.setchannels(1)
        self.inp.setrate(8000)
        self.inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

        # The period size controls the internal number of frames per period.
        # The significance of this parameter is documented in the ALSA api.
        # For our purposes, it is suficcient to know that reads from the device
        # will return this many frames. Each frame being 2 bytes long.
        # This means that the reads below will return either 320 bytes of data
        # or 0 bytes of data. The latter is possible because we are in nonblocking
        # mode.
        # Higher than 1600 appears to add a delay.  
        # Use a multiple of 8
        self.inp.setperiodsize(160)

    def is_sound(self):
        logging.debug("is_sound")
        # Read data from device
        length, data = self.inp.read()

        if length:
            # Return the maximum of the absolute value of all samples in a fragment.
            audio_val = audioop.max(data, 2)
            logging.debug("audio_val=" + str(audio_val))
            if audio_val > 1000:
                return True
        return False
