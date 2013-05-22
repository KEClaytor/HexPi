# Module that contains patters for the HexLight
from pattern import Pattern, Animation

def all_bits(state):
    return Pattern(repeat(state, 24))

def all_on():
    return all_bits(1)

def all_off():
    return all_bits(0)

def inner_circle():
    return Pattern(map(lambda x: x > 17, range(25)))

def inner_circle_alt_odd():
    return Pattern(map(lambda x: x > 17 and x % 2, range(25)))

def inner_circle_alt_even():
    return Pattern(map(lambda x: x > 17 and not x % 2, range(25)))

def outer_circle():
    return Pattern(map(lambda x: x < 18, range(25)))

def outer_circle_alt_odd():
    return Pattern(map(lambda x: x < 18 and x % 2, range(25)))

def outer_circle_alt_even():
    return Pattern(map(lambda x: x < 18 and not x % 2, range(25)))

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
