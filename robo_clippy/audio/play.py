# pylint: disable=E0401
# Disabling because OSX can't install pyaudio
 
import pyaudio
import wave
import logging
import alsaaudio, time, audioop
import audioop

class PlayAudio(object):

    inp = None
    servo = None
    frame_rate = 24000 # Frame rate from WAV returned by Cognitive Services
    period_size = 4000 # Frame rate / 8
    chunk_size = 4000
    time_between_movements = 0.16
    sound_format = alsaaudio.PCM_FORMAT_S16_LE
    audio_threshold = 1000

    def __init__(self, servo):
        logging.info("starting up")
        self.servo = servo
        # Open the device in nonblocking capture mode. The last argument could
        # just as well have been zero for blocking mode. Then we could have
        # left out the sleep call in the bottom of the loop
        self.inp = alsaaudio.PCM(device='default')

        # Set attributes: Mono, 8000 Hz, 16 bit little endian samples
        self.inp.setchannels(1)
        self.inp.setrate(self.frame_rate) # Frame rate from WAV returned by Cognitive Services
        self.inp.setformat(self.sound_format)

        # The period size controls the internal number of frames per period.
        # The significance of this parameter is documented in the ALSA api.
        # For our purposes, it is suficcient to know that reads from the device
        # will return this many frames. Each frame being 2 bytes long.
        # This means that the reads below will return either 320 bytes of data
        # or 0 bytes of data. The latter is possible because we are in nonblocking
        # mode.
        # Higher than 1600 appears to add a delay.  
        # Use a multiple of 8
        #self.inp.setperiodsize(320)
        self.inp.setperiodsize(self.period_size)

    def play_stream(self, stream):
        start_time = time.time()
        wf = wave.open(stream, 'rb')
        #print("sample width=" + str(wf.getsampwidth()))
        #print("frame rate=" + str(wf.getframerate()))
        data = wf.readframes(self.period_size)
        #print("The synthesized wave length: %d" %(len(data)))
        # http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
        while len(data) > 0:
            #print("Elapsed Time streaming: " + str(time.time() - start_time) + " len(data) = " + str(len(data)))
            start_time_write = time.time()
            self.inp.write(data)
            #print("Time to write: " + str(time.time() - start_time_write))

            # If we write too fast (which happens with audio jack), then the mouth stop moving too soon
            # This forced delay of .17 seconds per frame is about perfect to keep the mouth in sync with the audio
            #if (time.time() - start_time_write < self.time_between_movements):
            #    time.sleep(self.time_between_movements - (time.time() - start_time_write))

            data = wf.readframes(self.chunk_size)
            if self.is_sound(data):
                self.servo.speak()
            else:
                self.servo.mouth_neutral()

        # Stop stream.
        self.servo.mouth_neutral()
        stream.close()
        logging.info("Elapsed Time to stream audio: " + str(time.time() - start_time))

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