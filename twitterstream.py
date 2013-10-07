from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson
json = import_simplejson()
# Generic time
from time import sleep
from datetime import datetime
# RPi commands
import out
# TClock specific
import clock
import life
import misc
import re

# Import our keys
f = open('twitterkeys','r')
consumer_key =  f.readline().strip('\n')
consumer_secret = f.readline().strip('\n')
access_token = f.readline().strip('\n')
access_token_secret = f.readline().strip('\n')

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
    # comman was 'say'.
    if command == '' and options == '':
        command = 'say'
        options = text.replace('@tobleroneclock', '').lstrip()

    return command, options
    
def run_command(command,options):
    if command == 'clock':
        targetcmd = clock.clockmode()
    elif command == 'say':
        targetcmd = misc.clock_say(options)
    elif command == 'life':
        targetcmd = life.gameoflife()
    else:
        misc.tweethelp(command, options)

    targetcmd()
    return

class TobleroneListener (StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    cmd = "clock"
    opt = ""
    time = datetime.now()

    def on_data(self, data):
        ddata = json.loads(data)
        if "text" not in ddata:
            return True

        if "@tobleroneclock" not in ddata["text"]:
            return True

        self.cmd, self.opt = parse_command(ddata["text"])
        # Update the time-out timer
        self.time = datetime.now()

        return True

    def on_error(self, status):
        print status

class stop_monitor():
    def __init__(self):
        self.status = False
        return

    def set_continue(self):
        self.status = False
        return

    def set_stop(self):
        print "stop command received"
        self.status = True
        return

    def __call__(self):
        return self.status

if __name__ == '__main__':
    out.initialize()
    l = TobleroneListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # stream.filter(track=['basketball'])
    stream.userstream(async=True)
    cmd, opt = "clock",""

    while 1:
        print "current command: " + repr(l.cmd) + " " + repr(l.opt)

        sleep(10)
        # Go back to clock mode if we've spent time doing something else
        dt = l.time - datetime.now()
        if (cmd != "clock") and (dt.total_seconds() < -4*60):
            print "timeout occured, switching to clock mode"
            l.cmd = "clock"

	    # Don't do anything if the command and options haven't chnaged
        if (l.cmd == cmd) and (l.opt == opt):
            continue

        print "updating command: " + repr(l.cmd) + " " + repr(l.opt)
        cmd = l.cmd
        opt = l.opt

        # Reworking since we don't really need a thread
        run_command(cmd,opt)

