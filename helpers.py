#!/usr/bin/python
from math import sqrt, log
from itertools import count
import types
from operator import mul

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

def get_primes_less_than_p(p):
    """ Returns a list of prime numbers smaller than p
    Generating a list of primes for use by other functions
    prevents having to recheck for primeness."""
    primelist = [i for i in xrange(3, p, 2) if is_prime(i)]
    primelist.insert(0, 2)  # 2 is the smallest prime
    return primelist

def prime_factorization_tree(n):
    """ prime_factorization_tree(n) returns a list containing (base, exponent)
    tuples that make up the prime factorization of n"""

    if n == 1:
        return [(1, 0)]  # This is a kludge


    def get_factor_exponent(a, b):
        """ For factor b of a, returns the highest
        power of b that is divisible into a """
        max_power_possible = int(log(a, b)) + 1

        for i in xrange(max_power_possible, 0, -1):
            if not a % (b ** i):
                return i

    prime_less_than_n = get_primes_less_than_p(n)

    prime_factors = [x for x in prime_less_than_n if divisible(n,x)]
    if prime_factors == []:
        return [(n, 1)]
    remainder = n
    exponents = []

    for factor in prime_factors[::-1]:  # Do big factors first
        power = get_factor_exponent(remainder, factor)
        exponents.insert(0, power)
        remainder = int(remainder / (factor ** power))

    return zip(prime_factors, exponents)

def number_of_factors(n):
    """ Returns the number of factors for a given integer or
    prime factorization.  If the factorization is given, it 
    should follow the zip(factorlist, exponentlist) structure
    of prime_factorization_tree() output 

    We need to know that a number with prime factorization
    of the form n^a*p^b*q^c*... will have (a+1)(b+1)(c+1)*... factors.
    """

    if isinstance(n, types.ListType):
        return reduce(mul, [x[1] + 1 for x in n])
    elif isinstance(n, types.IntType):
        n = prime_factorization_tree(n)
        return reduce(mul, [x[1] + 1 for x in n])


def tri(n):
    """ Returns the nth triangular number"""
    return n * (n + 1) / 2

def triangle_generator():
    """ triangular number generator """
    for n in count(1, 1):
        yield tri(n)
