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
import clock
import out
import re
import stoppable

def parse_command(mon,thandle):
    text = thandle.get_mentions_text()
    print "Someone tweeted:  " + text
    try:
        command = re.match('.*:',text).group().strip(':')
    except:
        command = ''
    try:
        options = re.search(':.*',text).group().strip(':').lstrip()
    except:
        options = ''
    print command
    print options
    if command == 'clock':
        clockthread = stoppable.stoppable(mon.tweet_changed,\
            target=clock.clockmode)
    elif command == 'say':
        say(options)
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

def say(tw):
    for c in tw:
        if c not in ls.letter_dict:
            continue
        out.set_states_all(ls.letter_dict[c])
        sleep(1)
    return

class monitor_tweet:
    def __init__(self, thandle):
        self.thandle = thandle
        self.lasttweet = thandle.get_mentions_text()
    
    def tweet_changed(self):
        changed = 0
        if self.lasttweet != self.thandle.get_mentions_text():
            changed = 1
        return changed

def main():
    # Initalize Pi GPIO
    out.initialize()

    # Create a new twitter interface
    thandler = twitterclock.tclock()
    # Fake twitter for testing
    #thandler = twitterclock.fakeclock()
    monitor = monitor_tweet(thandler)

    while 1:
        #if monitor.tweet_changed():
        parse_command(monitor,thandler)

        # Twitter api rate limit is 100 / hr
        sleep(40)

    return

if __name__=="__main__":
    main()
