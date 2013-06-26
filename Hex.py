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

    lt = thandler.getmentiontext().lower()

    out.initialize()

    for c in lt:
        if c in ls.letter_dict:
            out.set_states_all(ls.letter_dict[c])
            sleep(1)
        else:
            continue

    while 1:
        tw = thandler.getmentiontext().lower()
        if (tw != lt):
            for c in tw:
                if c in ls.letter_dict:
                    out.set_states_all(ls.letter_dict[c])
                    sleep(1)
                else:
                    continue

        lt = tw
        # Twitter api rate limit is 100 / hr
        sleep(40)

    return

if __name__=="__main__":
    main()
