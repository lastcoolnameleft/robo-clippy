import os, time

class Listener(object):

    servo = None
    detect_audio = None
    pipe_path = "/tmp/clippy.pipe"

    def __init__(self, servo, detect_audio):
        self.servo = servo
        self.detect_audio = detect_audio

    def start(self):
        self.servo.neutral()
        if not os.path.exists(self.pipe_path):
            os.mkfifo(self.pipe_path)
        # Open the fifo. We need to open in non-blocking mode or it will stalls until
        # someone opens it for writting
        pipe_fd = os.open(self.pipe_path, os.O_RDONLY | os.O_NONBLOCK)
        print("Listening at " + self.pipe_path)
        with os.fdopen(pipe_fd) as pipe:
            while True:
                message = pipe.read()
                if message:
                    #print("Received: '%s'" % message)
                    self.process_message(message)

                audio_value = self.detect_audio.get_value()
                print("Received audio value: " + str(audio_value))
                if audio_value > 0:
                    self.servo.speak()
                else:
                    self.servo.mouth_neutral()
                time.sleep(.2)  # this needs to be .01 else the audio isn't read

    def process_message(self, message):
        if 'neutral' in message:
            self.servo.neutral()
        if 'excited' in message:
            self.servo.excited()
        if 'confused' in message:
            self.servo.confused()
        if 'angry' in message:
            self.servo.angry()
