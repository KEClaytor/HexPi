from out import *
from time import sleep

class Pattern:
    def __init__(self, bits):
        self.bits = bits
        return

    def draw(self):
        set_states_all(bits)
        return

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
        sleep(self.wait[self.frame])
        self.frame += 1

        return

    def animate(self):
        while 1:
            self.nextframe()
