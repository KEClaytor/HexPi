# Twitter control for our clock
# KEC 2013-06-24

import twitter

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

    # Returns unicode string of the last tweet to us
    def get_mentions_text(self):
        mentions = self.api.GetMentions()
        message = ''
        if len(mentions) > 0:
            men = mentions[0]
            rawtext = men.text
            message = rawtext.strip('@tobleroneclock ').lower()
        return message
        
    def get_mentions_user(self):
        mentions = self.api.GetMentions()
        user = ''
        if len(mentions) > 0:
            men = mentions[0]
            user = men.user.name
        return user

    # Posts to twitter needs write-enabled
    def post_text(self,text):
        rs = 0
        try:
            self.api.PostUpdate(text)
        except:
            rs = 1
            print "Unable to post update."
        return rs
