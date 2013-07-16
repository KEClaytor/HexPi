#miscelaneous hexlight output commands
# complicated enough for a file
# but not enough for a dedicated file

import out
import patterns
import twitterclock
import letters as ls
from time import sleep

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

class clock_idle:
    def __init__(self, n=2):
        idle_types = ['twinkle','spin_inner','spin_outer','spin_both','outer_inner']
        self.idle_type = idle_types[random.randint(0,len(idle_types))]
        self.n = n

    def __run__(self):
        #self.idle_type()
        pass

# Tweet help statements back to the user
def tweethelp(thandle, command, options):
    thandle = twitterclock.tclock()
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

