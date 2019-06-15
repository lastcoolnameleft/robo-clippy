# pylint: disable=E0401
# Disabling because OSX can't install pyaudio
 
import pyaudio
import wave
import alsaaudio, time, audioop
import audioop

class PlayAudio(object):

    inp = None
    servo = None
    chunk_size = 3840
    audio_threshold = 1000

    def __init__(self, servo):
        print("starting up")
        self.servo = servo
        # Open the device in nonblocking capture mode. The last argument could
        # just as well have been zero for blocking mode. Then we could have
        # left out the sleep call in the bottom of the loop
        self.inp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK, device='default')

        # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
        self.inp.setchannels(1)
        self.inp.setrate(24000) # Frame rate from WAV returned by Cognitive Services
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
        self.inp.setperiodsize(320)

    def play_stream(self, stream):
        start_time = time.time()
        wf = wave.open(stream)
        print('rate=' + str(wf.getframerate()))
        data = wf.readframes(self.chunk_size)
        print("The synthesized wave length: %d" %(len(data)))
        # http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
        while len(data) > 0:
            if self.is_sound(data):
                self.servo.speak()
            else:
                self.servo.mouth_neutral()
            self.inp.write(data)
            data = wf.readframes(self.chunk_size)

        # Stop stream.
        self.servo.mouth_neutral()
        stream.close()
        print("Elapsed Time to stream audio: " + str(time.time() - start_time))

        # DON'T CLOSE PyAudio.  If you do, it will SegFault the 3rd time you open it.
        #self.p.terminate()

    def is_sound(self, data):
        result = False
        if len(data):
            # Return the maximum of the absolute value of all samples in a fragment.
            audio_val = audioop.max(data, 2)
            #print("audio_val=" + str(audio_val))
            if audio_val > self.audio_threshold:
                result = True
        #print('is_sound();result=' + str(result))
        return result