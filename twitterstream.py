from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson
json = import_simplejson()
from time import sleep
from stoppable import stoppable
import Hex
import out

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

    def on_data(self, data):
        ddata = json.loads(data)
        if "text" not in ddata:
            return True

        if "@tobleroneclock" not in ddata["text"]:
            return True

        self.cmd, self.opt = Hex.parse_command(ddata["text"])

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
        print "updating command"
        print l.cmd, l.opt

        sleep(10)
	    # Make sure both command and options changed
        if (l.cmd == cmd) and (l.opt == opt):
            continue

        print "updating command and options"
        cmd = l.cmd
        opt = l.opt

        # Stop our clock thread
        sm.set_stop()
        # Wait until the thread's run has completed
        rt.join()
        # start the new command
        sm.set_continue()
        rt = Hex.run_command(sm,cmd,opt)
        rt.start()
