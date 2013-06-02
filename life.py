# Game of life routine for the HexLight
import random
from time import sleep 

# Import RPi stuff
import RPi.GPIO as GPIO
import out
import patterns

def dotprod(vec1,vec2):
    return sum(p*q for p,q in zip(vec1,vec2))

# Use bitwise xor to invert 1 <--> 0
def invvec(vec):
    return [(1,0)[x] for x in vec]

# Tests to see if two binary vectors are equal to each other
def eqvec(vec1,vec2):
    iseq = 1
    for x in range(len(vec1)):
        if vec1[x] != vec2[x]:
            iseq = 0
            break
    return iseq

# Adjacency matrix
Adjacent = [None]*21
for ii in range(21):
    Adjacent[ii] = [0]*21
for ii in range(20):
    Adjacent[ii][ii+1] = 1
# There is a disconnect
Adjacent[14][15] = 0
Adjacent[15][14] = 0
# Connecting innner to outer ring
Adjacent[0][14] = 1
Adjacent[0][15] = 1
Adjacent[3][16] = 1
Adjacent[5][17] = 1
Adjacent[7][19] = 1
Adjacent[13][20] = 1
Adjacent[15][20] = 1
# And the diagonally equivalent values
Adjacent[14][0] = 1
Adjacent[15][0] = 1
Adjacent[16][3] = 1
Adjacent[17][5] = 1
Adjacent[19][7] = 1
Adjacent[20][13] = 1
Adjacent[20][15] = 1

# TODO: Remove after testing
# Initalize Pi GPIO
GPIO.setmode(GPIO.BCM)
out.enable(GPIO.OUT)
patterns.all_off().draw()

# These should be input values
waits = 1    # waiting time in seconds
# Values related to survival of the element
str_self = 0 # self reinforcement
str_near = 2 # friendly reinforcement
str_nega = 0 # opposing color
thresh = 1   # Survivial threshold

# Initalize a random state vector
#  with n elements turned on
vec = [0]*21
non = 15
for x in range(non):
    ind = random.randint(0,20)
    # Make sure we have an empty spot
    while vec[ind]==1:
        ind = random.randint(0,20) 
    vec[ind] = 1

# Start the main loop though
out.set_states_all(vec)
print vec
while 1:
    sleep(waits)
    # See if this element survives
    newvec = [0]*21
    for x in range(len(newvec)):
        strength = str_self*vec[x] + str_near*dotprod(vec,Adjacent[x]) - str_nega*dotprod(invvec(vec),Adjacent[x])
        if strength > thresh:
            newvec[x] = 1
    # Check to see if there is a change
    if eqvec(vec,newvec):
        sleep(3)
        break
    vec = newvec
    out.set_states_all(vec)
    print vec

# TODO: remove after testing
# Housekeeping stuff with the IO ports
GPIO.cleanup()
