from out import *
from time import sleep

class Pattern:
    def __init__(self, bits):
        self.bits = map(int, bits)
        return

    def draw(self):
        set_states_all(self.bits)
        return

    def printscreen(self):
        textout(self.bits)
        return

    def __sub__(self, pin):
        tmpbits = self.bits
        tmpbits[pin] = 0
        return Pattern(tmpbits)

    def __add__(self, pin):
        tmpbits = self.bits
        tmpbits[pin] = 1
        return Pattern(tmpbits)


class Animation:
    def __init__(self, patterns, waits):
        self.patterns = patterns
        self.waits = waits
        self.nframes = len(patterns)
        self.frame = 0
        return

    def nextframe(self):
        if self.frame >= self.nframes:
            self.frame = 0

        self.patterns[self.frame].draw()
        sleep(self.waits[self.frame])
        self.frame += 1

        return

    def animate(self):
        while 1:
            self.nextframe()

    def printscreen(self):
	while 1:
            if self.frame >= self.nframes:
                self.frame = 0

            self.patterns[self.frame].printscreen()
            sleep(self.waits[self.frame])
            self.frame += 1

        return
