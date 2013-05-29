# Module that contains patters for the HexLight
from itertools import repeat
from pattern import Pattern, Animation

def all_bits(state):
    return Pattern(repeat(state, 21))

def all_on():
    return all_bits(1)

def all_off():
    return all_bits(0)

def inner_circle():
    return Pattern(map(lambda x: x > 14, range(21)))

def inner_circle_alt_odd():
    return Pattern(map(lambda x: x > 14 and x % 2, range(21)))

def inner_circle_alt_even():
    return Pattern(map(lambda x: x > 14 and not x % 2, range(21)))

def outer_circle():
    return Pattern(map(lambda x: x < 15, range(21)))

def outer_circle_alt_odd():
    return Pattern(map(lambda x: x < 15 and x % 2, range(21)))

def outer_circle_alt_even():
    return Pattern(map(lambda x: x < 15 and not x % 2, range(21)))

def wedge(wait):
	pass

# Twinkle n lights using base as the base color
def twinkle(wait,n,base):
	pass

# Spin a set of n lights around the outer wheel
def spinout(wait,n):
	pass

def spinin(wait,n):
	pass

def spinall(wait,n):
	pass

def spinning_inner_circle(wait):
    return Animation(
            [inner_circle_alt_odd(), inner_circle_alt_even()],
            [wait, wait])

def spinning_outer_circle(wait):
    return Animation(
            [outer_circle_alt_odd(), outer_circle_alt_even()],
            [wait, wait])
