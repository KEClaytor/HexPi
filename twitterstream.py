from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.utils import import_simplejson
json = import_simplejson()
from Hex import parse_command
from time import sleep
from stoppable import stoppable

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

        self.cmd, self.opt = parse_command(ddata["text"])

        return True

    def on_error(self, status):
        print status


def red_light():
    return True

def red_light():
    return False


if __name__ == '__main__':
    l = TobleroneListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # stream.filter(track=['basketball'])
    stream.userstream(async=True)

    while 1:
        print l.cmd, l.opt

        if l.cmd == cmd
            continue

        cmd = l.cmnd

        # TODO
        # stop previous stoppable.
        # start next stoppable.

        sleep(10)
