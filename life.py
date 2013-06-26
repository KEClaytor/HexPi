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

class gameoflife:
    def __init__(self, str_self=0, str_near=2.5, str_nega=1.5,
            thresh=1, numon=15, waits=1):
        self.str_self = str_self    # self reinforcement
        self.str_near = str_near    # friendly reinforcement
        self.str_nega = str_nega    # opposing color
        self.thresh = thresh        # survival threshold
        self.waits = waits          # waiting time in s

        # Initalize a random state vector
        #  with n elements turned on
        vec = [0]*21
        for x in range(numon):
            ind = random.randint(0,20)
            # Make sure we have an empty spot
            while vec[ind]==1:
                ind = random.randint(0,20) 
            vec[ind] = 1

        self.state = vec

        return

    def __call__(self):
        # See if this element survives
        vec = [0]*21
        for x in range(len(vec)):
            self.strength = self.str_self*self.state[x] + \
                    self.str_near*dotprod(self.state, Adjacent[x]) - \
                    self.str_nega*dotprod(invvec(self.state), Adjacent[x])

            if strength > self.thresh:
                vec[x] = 1

        self.state = vec
        out.set_states_all(self.state)

        sleep(self.waits)

        return
