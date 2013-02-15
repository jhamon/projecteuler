from __future__ import division
from math import sqrt
from operator import mul


def tri(n):
    return n*(n+1)/2

primelist = [2, 3]
i = 5
while len(primelist) < 10000:
    upperbound = int(sqrt(i)) + 1  # Only check to sqrt(n)
    for j in xrange(2, upperbound + 1):
        if i % j == 0:  # Divisible, so not prime
            break
        if j == upperbound:
            primelist.append(i)
            break
    i = i + 2  # increment by 2, to check odds only


def prime_tree(n):
    dividend = n
    factors = []
    i = 0
    while True:
        divisor = primelist[i]
        quotient = dividend / divisor
        if int(quotient) == quotient:
            factors.append(divisor)
            dividend = quotient
        elif int(quotient) != quotient:
            i = i + 1
        if quotient == 1:
            break
    return factors

i = 7
while True:
    factorlist = prime_tree(tri(i))
    outlist = map(factorlist.count, primelist)
    exponents = [x for x in outlist if x > 0]
    number_of_factors = reduce(mul, [x + 1 for x in exponents])
    # print i, number_of_factors
    if number_of_factors > 500:
    	break
    i = i + 1

print tri(i)
