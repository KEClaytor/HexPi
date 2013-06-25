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

# Initalize Pi GPIO
#out.initalize()
# Create a new twitter interface
thandler = twitterclock.tclock()

latesttweet = thandler.getmentiontext()
print latesttweet
