#!/usr/bin/python
from math import sqrt
from itertools import count

def is_prime(x):
	""" Slow method for determining whether a number is prime
	by checking all potential factors up to sqrt(x) until one
	is found"""
	if x == 1:
		return False
	elif x == 2:
		return True
	elif not x % 2: # Even number, not prime
		return False

	for i in range(3,int(sqrt(x))+1,2):
		if not x % i: 
		    # Evenly divisible, not prime
			return False
	else:
		return True 


def divisible(a, b):
    """Returns true if a divisible by b"""
    return not (a % b)


def gcd(x, y):
	""" returns greatest common divisor """
	if x < y:
		x, y = y, x

	while y:
		x, y = y, x % y
	return x

def lcm(x, y):
	""" returns the least common multiple """
	return x * y / gcd(x, y)

odd_gen = count(3, 2)
def prime_generator():
    """ Generator function emits one prime at a time"""
    genprimelist = [2]
    def _is_prime(n):
        factors = [n % x for x in genprimelist if x <= sqrt(n)]
        if 0 in factors:
        	return False
        else:
        	return True

    for x in odd_gen:
        if _is_prime(x):
            genprimelist.append(x)
            yield x