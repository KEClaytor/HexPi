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
import patterns
import clock
import out
import re
from stoppable import stoppable

def parse_command(thandle):
    text = thandle.get_mentions_text()
    print "Someone tweeted:  " + text
    try:
        command = re.search('.*:',text).group().rstrip(':').lstrip('@tobleroneclock').lstrip()
    except:
        command = ''
    try:
        options = re.search(':.*',text).group().lstrip(':').lstrip()
    except:
        options = ''
    # in the case that the user didn't specify a command, assume the
    # command was 'say'.
    if command == '' and options == '':
        command = 'say'
        options = text.lstrip('@tobleroneclock').lstrip()
    print command
    print options
    tm = tweet_monitor(thandle)
    if command == 'clock':
        newclock = clock.clockmode()
        clockthread = stoppable(tm, target=newclock)
        clockthread.run()
    elif command == 'say':
        saymessage = clock_say(options)
        saythread = stoppable(tm, target=saymessage)
        saythread.run()
    else:
        tweethelp(thandle, command, options)
    return 
    
# Tweet help statements back to the user
def tweethelp(thandle, command, options):
    user = thandle.get_mentions_user()
    if options == 'help':
        text = "tweet 'help: subject' where subject = {say,clock,life}"
    elif options == 'say':
        text = "say: string || prints out 'string' to the display"
    elif options == 'clock':
        text = "clock: options || enables clock-mode where options = {analog,digital}"
    elif options == 'life':
        text = "life: selfstr goodstr negastr threshold numberon waittime || all optional"
    else:
        text = "I don't understand you. Tweet 'help: help' for a list of commands."
    tweet = '@%s %s' % (user,text)
    # Check that we didn't just post this message - we don't want to spam
    lastpost = thandle.get_last_post()
    if not tweet == lastpost:
        thandle.post_text(tweet)
    return

class clock_say:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        print self.message
        for char in self.message:
            if char not in ls.letter_dict:
                continue
            out.set_states_all(ls.letter_dict[char])
            sleep(1)
            patterns.all_off().draw()
            sleep(0.05)
        sleep(5)
        return

class tweet_monitor:
    def __init__(self, thandle):
        self.thandle = thandle
        self.lasttweet = thandle.get_mentions_text()
    
    def __call__(self):
        changed = 0
        if self.lasttweet != self.thandle.get_mentions_text():
            changed = 1
            self.lasttweet = self.thandle.get_mentions_text()
        return changed

def main():
    # Initalize Pi GPIO
    out.initialize()

    # Create a new twitter interface
    thandler = twitterclock.tclock()
    # Fake twitter for testing
    #thandler = twitterclock.fakeclock()

    while 1:
        #if monitor.tweet_changed():
        parse_command(thandler)

        # Twitter api rate limit is 100 / hr
        sleep(30)

    return

if __name__=="__main__":
    main()
