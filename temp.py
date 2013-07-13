from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson
json = import_simplejson()
from time import sleep
from datetime import datetime
from stoppable import stoppable

class stop_monitor():
    def __init__(self):
        self.status = False

    def set_continue(self):
        print "continue command received"
        self.status = False
        return

    def set_stop(self):
        print "stop command received"
        self.status = True
        return

    def __call__(self):
        return self.status

class stupidprint():
    def __init__(self,myint):
        self.myint = myint
        return

    def __call__(self):
        print "still running " + repr(self.myint)
        sleep(3)
        return

if __name__ == '__main__':

    sm = stop_monitor()
    start = datetime.now()
    ctr = 1
    while 1:
        sleep(2)
        dt = datetime.now() - start
        print "elapsed seconds: " + repr(dt.seconds)
        print sm()

        if dt.seconds < 15:
            continue
        ## Create a stop monitor and send it to the
        ## class that creats the command and thread
        ## stop previous stoppable.
        sm.set_stop()
        print "stopping sm: " + repr(sm())
        print "resetting time"
        start = datetime.now()
        ctr += 1
        sleep(2)
        ## start next stoppable.
        sm.set_continue()
        print "starting sm: " + repr(sm())
        mytarget = stupidprint(ctr)
        rt = stoppable(sm,target=mytarget)
        rt.run()
 
