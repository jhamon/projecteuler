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