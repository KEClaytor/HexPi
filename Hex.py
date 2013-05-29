#!/usr/bin/env python

# Main control code for the HexLight
# 2013-04-23 Kevin Claytor

# Import RPi stuff
import RPi.GPIO as GPIO

# Import modules for patterns
import patterns
#import letters
from time import sleep

# Import modules for twitter commands
import out

# Initalize Pi GPIO
GPIO.setmode(GPIO.BCM)
out.enable(GPIO.OUT)

# Loop through each of them, turning them on one at a time
#all_on().draw()
#sleep(1)
patterns.all_off().draw()
#sleep(1)

# A little routine for figuring out the mapping of the dictionary
while 1:
    for pin in range(21):
        out.set_state(pin,1)
        sleep(1)
        out.set_state(pin,0)

# c = patterns.spinning_outer_circle(1)
c = patterns.spinning_inner_circle(1)
c.animate()

