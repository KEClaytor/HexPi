#!/usr/bin/env python
# Main control code for the HexLight
# 2013-04-23 Kevin Claytor

# Generic imports
from time import sleep

# Import twitter methods
import patterns
import clock
import life
import misc
import out
import re
from stoppable import stoppable

def parse_command(text):
    # Try parsing the command
    try:
        command = re.search('.*:',text).group().rstrip(':').replace('@tobleroneclock','').lstrip()
    except:
        command = ''
    # and the options
    try:
        options = re.search(':.*',text).group().lstrip(':').lstrip()
    except:
        options = ''

    # in the case that the user didn't specify a command, assume the
    # command was 'say'.
    if command == '' and options == '':
        command = 'say'
        options = text.replace('@tobleroneclock', '').lstrip()

    return command, options
    
def run_command(stop_mon,command,options):
    if command == 'clock':
        targetcmd = clock.clockmode()
    elif command == 'say':
        targetcmd = misc.clock_say(options)
    elif command == 'life':
        targetcmd = life.gameoflife()
    else:
        misc.tweethelp(command, options)

    print "Creating thread with command: " + command

    run_thread = stoppable(stop_mon, target=targetcmd)
    return run_thread

def main():
    pass
    ## Initalize Pi GPIO
    #out.initialize()

    ## Create a new twitter interface
    #thandler = twitterclock.tclock()
    ## Fake twitter for testing
    ##thandler = twitterclock.fakeclock()

    #while 1:
    #    #if monitor.tweet_changed():
    #    parse_command(thandler)

    #    # Twitter api rate limit is 100 / hr
    #    sleep(30)

    #return

if __name__=="__main__":
    # update: run twitterstream.py as the main class
    main()
