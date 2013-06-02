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

c = patterns.spinning_inner_circle(1)
c.animate()
sleep(10)

