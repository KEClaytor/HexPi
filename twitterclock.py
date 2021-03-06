# Twitter control for our clock
# KEC 2013-06-24

import twitter
import random
from datetime import datetime

class tclock:
    def __init__(self):
        # We could pass these in as args, but currently
        # this will only be used as the toblerone clock
        f = open('twitterkeys','r')
        self.consumer_key =  f.readline().strip('\n')
        self.consumer_secret = f.readline().strip('\n')
        self.access_token = f.readline().strip('\n')
        self.access_token_secret = f.readline().strip('\n')
        
        self.api = twitter.Api(consumer_key=self.consumer_key, \
            consumer_secret=self.consumer_secret, \
            access_token_key=self.access_token, \
            access_token_secret=self.access_token_secret)
        # Store the last few mentions and only update them
        # infrequently
        self.last_access_time = datetime.now()
        self.mentions = self.api.GetMentions()
        self.update_time = 120

    def get_api(self):
        return self.api

    # Updates the mentions
    def update(self):
        elapsed = datetime.now() - self.last_access_time
        if elapsed.seconds > self.update_time:
            self.mentions = self.api.GetMentions()
        return

    # Returns unicode string of the last tweet to us
    def get_mentions_text(self):
        self.update()
        message = ''
        if len(self.mentions) > 0:
            men = self.mentions[0]
            rawtext = men.text
            message = rawtext.lower()
        return message
        
    def get_mentions_user(self):
        self.update()
        user = ''
        if len(mentions) > 0:
            men = self.mentions[0]
            user = men.user.screen_name
        return user

    def get_last_post(self):
        mytweets = self.api.GetHomeTimeline()
        lastpost = mytweets[0].text
        return lastpost

    # Posts to twitter needs write-enabled
    def post_text(self,text):
        rs = 0
        try:
            self.api.PostUpdate(text)
        except:
            rs = 1
            print "Unable to post update."
        return rs

class fakeclock:
    def __init__(self):
        # We could pass these in as args, but currently
        # this will only be used as the toblerone clock
        self.messages = ['help: help',\
                'clock:','help: clock',\
                'say: love gleb',\
                'watching star wars',\
                'say: clockmode (Oh, I''m evil)']
        self.users = ['test_keclaytor','test_cspollard']
        self.lastmessage = \
            self.messages[random.randint(0,len(self.messages)-1)]

    # Returns unicode string of the last tweet to us
    def get_mentions_text(self):
        if random.random() > .9:
            message = \
                self.messages[random.randint(0,len(self.messages)-1)]
            self.lastmessage = message
        else:
            message = self.lastmessage
        return '@tobleroneclock ' + message
        
    def get_last_post(self):
        return '@tobleroneclock ' + self.lastmessage

    def get_mentions_user(self):
        user = self.users[random.randint(0,len(self.users)-1)]
        return user

    # Posts to twitter needs write-enabled
    def post_text(self,text):
        print text
        rs = 0
        return rs
