# Find the sum of all primes smaller than 2 million

from math import sqrt

def is_prime(n):
	factors_to_check = xrange(3,int(sqrt(n))+1,2)
	for fac in factors_to_check:
		if not n % fac:
			return False
	else:
		return True

primelist = [i for i in xrange(3,2000000,2) if is_prime(i)]
primelist.insert(0,2) # 2 is the smallest prime
print sum(primelist) # Answer: 142913828922