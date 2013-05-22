#!/usr/bin/env python

# Main control code for the HexLight
# 2013-04-23 Kevin Claytor

# Import RPi stuff
import RPi.GPIO as GPIO

# Import modules for patterns
import patterns
import letters
from time import sleep

# Import modules for twitter commands
import out

# Initalize Pi GPIO
GPIO.setmode(GPIO.BCM)
out.enable(GPIO.OUT)

# Begin running the main loop


