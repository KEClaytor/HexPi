from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson
json = import_simplejson()
from time import sleep
from stoppable import stoppable
import Hex
import out
from datetime import datetime

# Import our keys
f = open('twitterkeys','r')
consumer_key =  f.readline().strip('\n')
consumer_secret = f.readline().strip('\n')
access_token = f.readline().strip('\n')
access_token_secret = f.readline().strip('\n')

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

        self.cmd, self.opt = Hex.parse_command(ddata["text"])
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

    # Start an initial clock thread
    sm = stop_monitor()
    rt = Hex.run_command(sm,cmd,opt)
    rt.start()
    while 1:
        print "current command: " + repr(l.cmd) + " " + repr(l.opt)

        sleep(10)
        # Go back to clock mode if we've spent time doing something else
        dt = l.time - datetime.now()
        if (l.cmd != "clock") and (dt.minutes > 2):
            print "timeout occured, switching to clock mode"
            l.cmd = "clock"

	    # Don't do anything if the command and options haven't chnaged
        if (l.cmd == cmd) and (l.opt == opt):
            continue

        print "updating command: " + repr(l.cmd) + " " + repr(l.opt)
        cmd = l.cmd
        opt = l.opt

        # Stop our thread
        sm.set_stop()
        # Wait until the thread's run has completed
        rt.join()
        # start the new command
        sm.set_continue()
        rt = Hex.run_command(sm,cmd,opt)
        rt.start()

