# Some useful debugging methods
import out
import patterns
import clock
import datetime
from time import sleep

# Loop through each of pin, turning them on one at a time
def debug_loopall():
    while True:
        for i in range(21):
            patterns.all_off().draw()
            out.set_state(i,1)
            sleep(.5)
    return
        
    patterns.all_off().draw()
    clockmode()
    return

# Echo the keyboard
def debug_echo():
    while True:
        char = raw_input()
        if char in letter_dict:
            out.set_states_all(letter_dict[char])
    return

# Run clock mode in fast-forward
def debug_clock():
    for hour in range(24):
        for minute in range(60):
            clockstate = clock.setface(hour,minute)
            out.set_states_all(clockstate)
            # we only have to update once a resolution cycle
            ut = clock.RESMIN - \
                (minute - (minute/clock.RESMIN)*clock.RESMIN )
            # Print out text to double check
            print ""
            print "current hour: " + repr(hour)
            print "current minute: " + repr(minute)
            print "resolution: " + repr(RESMIN)
            print clockstate
            print "next update in: " +repr(ut) + " min"
            sleep(.1)
    return

