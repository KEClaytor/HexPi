# Output functions
#__out_dict = dict(enumerate(range(22)))
# I'm not sure if this is the right way to do it, but these are the pin numberings
# They do not correspond to the order in the numberings below
# This is the dictionary for BCM numbering
__out_dict = dict(enumerate([27,18,29,7,28,8,11,25,9,31,10,24,23,22,30,4,14,15,17,2,3]))
# And this is the dictionary for BOARD numbering
# I'm not sure how to address the P5 header, so I'll leave those as 0 for now...?
# __out_dict = dict(enumerate([3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,26,0,0,0,0]))

# Import RPi GPIO 
import RPi.GPIO as GPIO

from itertools import repeat

# Lights are numbered as follows;
#         (02)  (04)
#      (01)  (03)  (05)
#      (18)  (19)  (06)
#   (17)  (24)  (20)  (07)
#   (16)  (23)  (21)  (08)
#      (15)  (22)  (09)
#      (14)  (12)  (10)
#         (13)  (11)

#   0 0
#  0 0 0
#  0 0 0 
# 0 0 0 0
# 0 0 0 0
#  0 0 0
#  0 0 0 
#   0 0

# Text out to the screen (useful while we're building)
# To compressed, lengthen it out a bit
def textout(hc):
    print " "+repr(hc[0])+repr(hc[1])+repr(hc[2])+repr(hc[3])+repr(hc[4])
    print ""+repr(hc[16])+repr(hc[17])+repr(hc[18])+repr(hc[19])+repr(hc[20])+repr(hc[5])+repr(hc[6])
    print ""+repr(hc[15])+repr(hc[14])+repr(hc[23])+repr(hc[22])+repr(hc[21])+repr(hc[8])+repr(hc[7])
    print " "+repr(hc[13])+repr(hc[12])+repr(hc[11])+repr(hc[10])+repr(hc[9])
    return

# Actual output on the GPIO of the Pi
def lightout(hc):
    pass

# Enable all IO pins on the Pi
def enable(state):
    # setmode should only be called once
    #GPIO.setmode(GPIO.BCM)
    for pin in range(21):
        GPIO.setup(__out_dict[pin], state)
    return

def set_state(pin, state):
    # For debugging:
    # print repr(pin) + " = " + repr(__out_dict[pin]) + " -> " + repr(state)
    GPIO.output(__out_dict[pin], state)
    return

def set_states_lists(pins, states):
    map(set_state, pins, states)
    return

def set_states_pairs(pstates):
    set_state_lists(zip(*pstates))
    return

def set_states_all(states):
    set_states_lists(range(21), states)
    return
