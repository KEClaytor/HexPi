# Twitter control for our clock
# KEC 2013-06-24

import twitter

class tclock:
    def __init__(self):
        # We could pass these in as args, but currently
        # this will only be used as the toblerone clock
        self.consumer_key = \
            'nnlC6vCYrtNutwPioKdsw'
        self.consumer_secret = \
            'pD6xIzkYG2FDiDIWuQAomODpkAlwY6A12BbZnoY'
        self.access_token = \
            '1514508019-ltdrcX9lMdMvlhxobpRMNNK1M5OvlBwX3tojpyY'
        self.access_token_secret = \
            'ld9ToWtNKRruZkozy8oJGFizwrtQsqOp8aEGncP1w'
        
        self.api = twitter.Api(consumer_key=self.consumer_key, \
            consumer_secret=self.consumer_secret, \
            access_token_key=self.access_token, \
            access_token_secret=self.access_token_secret)

    # Returns unicode string of the last tweet to us
    def getmentiontext(self):
        mentions = self.api.GetMentions()
        if len(mentions) > 0:
            men = mentions[0]
            rawtext = men.text
            message = rawtext.strip('@tobleroneclock ')
            return message

    # Posts to twitter needs write-enabled
    def posttext(self,text):
        try:
            self.api.PostUpdate(text)
        except:
            rs = 1
            print "Unable to post update."
        return rs
