# Use the face of the HexLight as a clock

from datetime import datetime
from time import sleep
import out

# resolution based on the number of elements we have
# note: we'll actually get twice this resolution
#       as we'll link two elements together
NHR = 6
RESHR = 12/NHR    # 12 hours, 6 inner elments = 2 hour resolution
NMN = 15
RESMIN = 60/NMN

def setface(hour,minute):
    timevec = [0]*21
    # if we're in the PM change the background color
    if hour >= 12:
        cval = 0
        hour -= 12
        for x in range(21):
            timevec[x] = 1
    else:
        cval = 1
    # set the hour
    timevec[hour/RESHR+NMN] = cval
    # if we're odd set the next element, so we bridge two
    if hour%2 != 0:
        timevec[((hour/RESHR)+1)%NHR+NMN] = cval
    # set the minute
    timevec[minute/RESMIN] = cval
    return timevec

def clockmode():
    while 1:
        #for minute in range(60):
        print datetime.now()
        hour = datetime.now().hour
        minute = datetime.now().minute
        clockstate = setface(hour,minute)
        out.set_states_all(clockstate)
        # we only have to update once a resolution cycle
        ut = RESMIN - (minute - (minute/RESMIN)*RESMIN )
        # debugging
        print ""
        print "current hour: " + repr(hour)
        print "current minute: " + repr(minute)
        print "resolution: " + repr(RESMIN)
        print clockstate
        print "next update in: " +repr(ut) + " min"
        # Update on second after when we should to make sure we update propertly
        sleep(ut*60+1)
