# pylint: disable=E0401
# Disabling because OSX can't install alsaaudio

## This is an example of a simple sound capture script.
##
## The script opens an ALSA pcm for sound capture. Set
## various attributes of the capture, and reads in a loop,
## Then prints the volume.
##
## To test it out, run it and shout at your microphone:

import alsaaudio
import audioop

class DetectAudio(object):

    inp = None

    def __init__(self):
        print("starting up")
        # Open the device in nonblocking capture mode. The last argument could
        # just as well have been zero for blocking mode. Then we could have
        # left out the sleep call in the bottom of the loop
        self.inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

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
        self.inp.setperiodsize(3200)

    def get_value(self):
        # Read data from device
        l,data = self.inp.read()
        
        if l:
            # Return the maximum of the absolute value of all samples in a fragment.
            return audioop.max(data, 2)
        else:
            return 0