# Output functions
# I'm not sure if this is the right way to do it, but these are the pin numberings
# They correspond to the order in the schematic below
# This is the dictionary for BCM numbering
__out_dict = dict(enumerate([27,18,29,7,28,8,11,25,9,31,10,24,23,22,30,4,14,15,17,2,3]))

# Import RPi GPIO 
try:
    import RPi.GPIO as GPIO
    USEPI = True
    print "loaded GPIO"
except ImportError:
    USEPI = False
    print "did not load GPIO"

from itertools import repeat

# Lights are numbered as follows;
#         (14)  (01)
#      (14)  (00)  (02)
#      (13)  (15)  (03)
#   (12)  (20)  (16)  (04)
#   (11)  (19)  (17)  (04)
#      (10)  (18)  (05)
#      (09)  (08)  (06)
#         (09)  (07)

# Text out to the screen (useful while we're building)
def textout(hc):
    print " "+repr(hc[14])+repr(hc[14])+repr(hc[0])+repr(hc[1])+repr(hc[2])
    print ""+repr(hc[12])+repr(hc[13])+repr(hc[20])+repr(hc[15])+repr(hc[16])+repr(hc[3])+repr(hc[4])
    print ""+repr(hc[11])+repr(hc[10])+repr(hc[19])+repr(hc[18])+repr(hc[17])+repr(hc[5])+repr(hc[4])
    print " "+repr(hc[9])+repr(hc[9])+repr(hc[8])+repr(hc[7])+repr(hc[6])
    return

# Enable all IO pins on the Pi
def enable(state):
    # setmode should only be called once
    pass

# Initalize the IO pins
def initialize():
    if USEPI:
        GPIO.setmode(GPIO.BCM)
        #GPIO.enable(GPIO.OUT)
        #GPIO.setmode(GPIO.BCM)
        for pin in range(21):
            GPIO.setup(__out_dict[pin], GPIO.OUT)
    return

def set_state(pin, state):
    if USEPI:
        GPIO.output(__out_dict[pin], state)
    else:
        print repr(pin) + " = " + repr(__out_dict[pin]) + " -> " + repr(state)
    return

def set_states_lists(pins, states):
    map(set_state, pins, states)
    return

def set_states_pairs(pstates):
    set_state_lists(zip(*pstates))
    return

def set_states_all(states):
    if USEPI:
        set_states_lists(range(21), states)
    else:
        textout(states)
    return
