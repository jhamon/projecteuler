#!/usr/bin/python
from math import sqrt

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