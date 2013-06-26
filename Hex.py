#!/usr/bin/env python
# Main control code for the HexLight
# 2013-04-23 Kevin Claytor

# Generic imports
from time import sleep

# Raw output method to the pins
#import out
# Import patters, letters, and the clock
#import patterns
#import letters
#import clock

# Import twitter methods
import twitterclock
import letters as ls
import out

def main():
    # Initalize Pi GPIO
    #out.initalize()
    # Create a new twitter interface
    thandler = twitterclock.tclock()

    lt = thandler.getmentiontext()

    out.initialize()

    while 1:
        tw = thandler.getmentiontext()
        if (tw != lt):
            for c in tw:
                out.set_states_all(ls.letter_dict[c])

        lt = tw
        sleep(10)

    return

if __name__=="__main__":
    main()
