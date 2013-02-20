from nose.tools import *
from helpers import *

def test_is_prime():
	eq_(is_prime(1), False)
	eq_(is_prime(2), True)
	eq_(is_prime(5), True)
	eq_(is_prime(7), True)
	eq_(is_prime(9), False)
	eq_(is_prime(11), True)
	eq_(is_prime(16), False)
	eq_(is_prime(49), False)

def test_gcd():
	eq_(gcd(5, 25), 5)
	eq_(gcd(2, 11), 1)
	eq_(gcd(4, 16), 4)
	eq_(gcd(100, 125), 25)
	eq_(gcd(25, 5), 5)
	eq_(gcd(11, 5), 1)

def test_lcm():
	eq_(lcm(2, 5), 10)
	eq_(lcm(10, 20), 20)
	eq_(lcm(20, 10), 20)
	eq_(lcm(30, 14), 210)
	eq_(lcm(3, 9), 9)