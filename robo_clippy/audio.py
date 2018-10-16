# pylint: disable=E0401
# Disabling because OSX can't install pyaudio
 
import pyaudio
import wave

from ctypes import *
from contextlib import contextmanager

class Audio(object):

    p = None

    def __init__(self):
        ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

        def py_error_handler(filename, line, function, err, fmt):
            pass

        c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

        @contextmanager
        def noalsaerr():
            asound = cdll.LoadLibrary('libasound.so')
            asound.snd_lib_error_set_handler(c_error_handler)
            yield
            asound.snd_lib_error_set_handler(None)
        with noalsaerr():
            self.p = pyaudio.PyAudio()

    def play_stream(self, stream):
        wf = wave.open(stream)
        #p = pyaudio.PyAudio()
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()), 
                             channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
        CHUNK_SIZE = 1024
        data = wf.readframes(CHUNK_SIZE)
        print("The synthesized wave length: %d" %(len(data)))
        # http://code.activestate.com/recipes/579116-use-pyaudio-to-play-a-list-of-wav-files/
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK_SIZE)

        # Stop stream.
        stream.stop_stream()
        stream.close()

        # Close PyAudio.
        self.p.terminate()

