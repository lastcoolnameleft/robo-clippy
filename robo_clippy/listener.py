import os, time

class Listener(object):

    servo = None
    pipe_path = "/tmp/clippy.pipe"

    def __init__(self, servo):
        self.servo = servo

    def start(self):

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
                    print("Received: '%s'" % message)
                    self.process_message(message)
                # print("Doing other stuff")
                time.sleep(1)

    def process_message(self, message):
        if 'neutral' in message:
            self.servo.neutral()
        if 'excited' in message:
            self.servo.excited()
        if 'confused' in message:
            self.servo.confused()
        if 'angry' in message:
            self.servo.angry()
