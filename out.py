# Output functions

# Import RPi GPIO 
import RPi.GPIO as GPIO

# Lights are numbered as follows;
#         (02)  (04)
#      (01)  (03)  (05)
#      (18)  (19)  (06)
#   (17)  (24)  (20)  (07)
#   (16)  (23)  (21)  (08)
#      (15)  (22)  (09)
#      (14)  (12)  (10)
#         (13)  (11)

#   0 0
#  0 0 0
#  0 0 0 
# 0 0 0 0
# 0 0 0 0
#  0 0 0
#  0 0 0 
#   0 0

# Text out to the screen (useful while we're building)
# To compressed, lengthen it out a bit
def textout(hc):
	print " "+repr(hc[0])+repr(hc[1])+repr(hc[2])+repr(hc[3])+repr(hc[4])
	print ""+repr(hc[16])+repr(hc[17])+repr(hc[18])+repr(hc[19])+repr(hc[20])+repr(hc[5])+repr(hc[6])
	print ""+repr(hc[15])+repr(hc[14])+repr(hc[23])+repr(hc[22])+repr(hc[21])+repr(hc[8])+repr(hc[7])
	print " "+repr(hc[13])+repr(hc[12])+repr(hc[11])+repr(hc[10])+repr(hc[9])
	return 0

# Actual output on the GPIO of the Pi
def lightout(hc):
	pass

# Enable all IO pins on the Pi
def enable(state):
    GPIO.setmode(GPIO.BCM)
    for pin in range(1,21)
        GPIO.setup(pin, state)

def onoff_led(PINS,state):
    # In this case PINS will be our state vector
    # And we really need to get the index of PINS when setting
    for PIN in PINS:
        GPIO.output(PIN,state)
    return 0
