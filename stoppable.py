from threading import Thread
from datetime import datetime

class stoppable (Thread):
    def __init__(self, stop, group=None, target=None, name=None,
            args=(), kwargs={}):
        Thread.__init__(self, group=group, target=target, name=name,
                args=args, kwargs=kwargs)

        # stop should be a function that tells the class when to stop.
        self.stop = stop
        self.target = target

        return


    def run(self):
        while 1:
            if self.stop():
                return

            self.target()

        return

class stopTimer:
    def __init__(self, timeout=5):
        self.starttime = datetime.now()
        self.timeout = timeout

    def __call__(self):
        elapsed = datetime.now() - self.starttime
        timeout = 0
        if elapsed.seconds > self.timeout:
            timeout = 1

