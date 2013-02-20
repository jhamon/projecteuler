#!/usr/bin/python
from __future__ import division
import helpers as help
from operator import mul
from math import sqrt, log
from itertools import count
from numpy import loadtxt


def problem1():
    """Print the sum of the numbers less than 1000 which are
       divisible by 3 or 5"""
    return sum([x for x in xrange(0, 1000) if x % 5 == 0 or x % 3 == 0])


def problem2():
    """ Returns the sum of all fibonacci numbers less than 4 million"""
    fibs = [1, 1]
    while fibs[-1] < 4000000:
        fibs.append(fibs[-1] + fibs[-2])
    fibs = fibs[:-1]

    return sum([x for x in fibs if x % 2 == 0])


def problem3(N=600851475143):
    """What is the largest prime factor of the number N = 600851475143 ?

    This solution will make use of the fact that a number is prime if it
    has no prime factors smaller than sqrt(n). Potential factors are checked
    from high to low, decrementing by 2 because N is not even.
    """
    check_factor = int(sqrt(N))
    while True:
        if help.divisible(N,check_factor) and help.is_prime(check_factor):
            return check_factor
        else:
            check_factor -= 1

def problem4():
    """Find the largest palindrome formed as the product of
    two 3-digit numbers"""

    a = range(1000, 900, -1)
    b = a
    pals = []
    for factor1 in a:
        for factor2 in b:
            prod = factor2 * factor1
            if str(prod)[::-1] == str(prod):
                pals.append(prod)
    return max(pals)


def problem5():
    """This problem asks us to find the least common multiple of all numbers less than 20."""
    mult = 1
    for x in range(1,20):
        mult = help.lcm(mult,x)
    return mult

def problem6():
    """ Find the difference between the sum of the squares of the first
    one hundred natural numbers and the square of the sum."""
    def square(x):
        return x ** 2

    sumofsquares = sum(map(square, xrange(1, 101)))
    squareofsum = square(sum(xrange(1, 101)))
    return (squareofsum - sumofsquares)


def problem7():
    """ The 10001st prime number"""
    primelist = [2, 3]
    i = 5
    while len(primelist) < 10001:
        if help.is_prime(i):
            primelist.append(i)
        i = i + 2  # increment by 2, to check odds only
    return primelist[-1]


def problem8():
    from operator import mul
    data = '731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208855111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

    maxprod = 0
    for i in xrange(0, 995):
        sublist = map(int, data[i:i + 5])
        if 0 in sublist:
            i = i + 9  # don't check products containing zero
            continue
        prod = reduce(mul, sublist)
        if prod > maxprod:
            maxprod = prod
    return maxprod


def problem9():
    """ Find a pythagorean triple with a+b+c = 1000

    # a**2 + b**2 == c**2
    # therefore, a**2 == c**2 - b**2
    # a**2 = (c-b)(c+b)
    #   P.S. I now see the solution is just 25x 8-15-17 triangle. Lame.
    """

    from itertools import permutations

    b = xrange(1, 500)
    perms = permutations(b, 2)
    for p in perms:
        if p[1] > p[0]:
            B, C = p[0], p[1]
            diffsq = (C - B) * (C + B)
            sqrtdiffsq = sqrt(diffsq)
            if sqrtdiffsq + B + C == 1000:
                return sqrtdiffsq * B * C
                break


def problem10():
    """Find the sum of all primes smaller than 2 million"""

    primelist = [i for i in xrange(3, 2000000, 2) if help.is_prime(i)]
    primelist.insert(0, 2)  # 2 is the smallest prime
    return sum(primelist)


def problem11():
    data = loadtxt('11.txt')
    # vertical
    v = max([reduce(mul, data[i:i + 4, j]) for i in xrange(0, 20 - 3) for j in xrange(0, 20)])

    # horizontal
    h = max([reduce(mul, data[i, j:j + 4]) for i in xrange(0, 20) for j in xrange(0, 20 - 3)])

    # Diagonal 1
    diag1 = max([reduce(mul, [data[i, j], data[i + 1, j + 1], data[i + 2, j + 2], data[i + 3, j + 3]]) for i in xrange(0, 17) for j in xrange(0, 17)])

    # Diagonal 2
    diag2 = max([reduce(mul, [data[i, j], data[i - 1, j - 1], data[i - 2, j - 2], data[i - 3, j - 3]]) for i in xrange(0, 17) for j in xrange(0, 17)])

    return max([v, h, diag1, diag2])


def problem12():
    """Problem: find the first triangular number with more
    than 500 factors.

    We need to know that a number with prime factorization
    of the form n^a*p^b*q*c will have (a+1)(b+1)(c+1) factors.
    This general pattern holds true even for numbers with many
    prime factors."""

    PRIME_LIST_MAX = 10000

    def tri(n):
        """ Returns the nth triangular number"""
        return n * (n + 1) / 2

    def triangle_generator():
        """ triangular number generator """
        for n in count(3, 1):
            yield n * (n + 1) / 2

    def gen_primes_less_than_p(p):
        """ Returns a list of prime numbers smaller than p
        Generating a list of primes for use by other functions
        prevents having to recheck for primeness."""
        primelist = [i for i in xrange(3, p, 2) if is_prime(i)]
        primelist.insert(0, 2)  # 2 is the smallest prime
        return primelist

        primelist = gen_primes_less_than_p(PRIME_LIST_MAX)

    def prime_factorization_tree(n):
        """ prime_factorization_tree(n) returns a list containing (base, exponent)
        tuples that make up the prime factorization of n"""

        divisible = help.divisible

        def get_factor_exponent(a, b):
            """ For factor b of a, returns the highest
            power of b that is divisible into a """
            max_power_possible = int(log(a, b)) + 1

            for i in xrange(max_power_possible, 0, -1):
                print 'Checking {0} / {1}**{2}'.format(a, b, i)
                if not a % (b ** i):
                    return i
                else:
                    print '{0} is not divisible by {1}'.format(a, b)

                    prime_factors = [x for x in primelist if x <= n and divisible(n, x)]
                    remainder = n
                    exponents = []

                    for factor in prime_factors[::-1]:  # Do big factors first
                        power = get_factor_exponent(remainder, factor)
                        exponents.insert(0, power)
                        remainder = int(remainder / (factor ** power))

                    return zip(prime_factors, exponents)

    def number_of_factors(factorization):
        """ Takes tuple list output of prime_factorization_tree and returns
        the number of factors that number has. """
        return reduce(mul, [x[1] + 1 for x in factorization])

    nof = 0
    triangle = triangle_generator()

    for tri in triangle:
        primefac = prime_factorization_tree(tri)
        nof = number_of_factors(primefac)
        if nof > 500:
            return int(tri)
            


def problem13():
    """Work out the first ten digits of the sum of the one-hundred
    50-digit numbers stored in 13.dat."""
    data = loadtxt('13.dat')
    bigsum = sum(data)
    return int(''.join(str(bigsum)[0:11].split('.')))


def problem15():
    """ Number of lattice paths from top left to bottom right """
    n = 5
    hist = [[1], [-1]]
    for t in xrange(0, 2 * n):
        for i in xrange(0, len(hist)):
            if hist[i].count(1) == n:
                hist[i] = hist[i] + [-1]
            elif hist[i].count(-1) == n:
                hist[i] = hist[i] + [1]
            else:
                hist.append(hist[i])
                hist[i] = hist[i] + [1]
                hist[-1] = hist[-1] + [-1]

    # print 'goal: ', n, len(hist), len(hist)/(2**(2*n-1)-len(hist))
    return len(hist) / (2 ** (2 * n - 1) - len(hist))


def problem16():
    """ Sum of digits of 2**1000"""

    return sum(map(int, list(str(2 ** 1000))))


def problem17():
    # How many letters are needed to write out the name
    # of numbers from 1 to 1000, following the British usage of
    # including "and" all over the place. e.g. one hundred AND five.
    ns = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        '100': 'hundred',
        '1000': 'one thousand'}

    def n2s(n):
        return ns[str(int(n))]

    def printXX():
        totalstr = ''
        for i in range(1, 100):
            if i < 21:
                totalstr = totalstr + n2s(i)
            elif i % 10 == 0:
                totalstr = totalstr + n2s(i)
            else:
                totalstr = totalstr + n2s(i - i % 10) + n2s(i % 10)
        return len(list(totalstr))

    zero2ninetynine = printXX()

    def hundreds():
        hundredsstr = ''
        for i in range(100, 1000, 100):
        # print i, n2s(i/100)+n2s(100)
            hundredsstr = hundredsstr + n2s(i / 100) + n2s(100)
        return len(list(hundredsstr))

    hundredsstr = hundreds()
    ands = len(range(1, 100)) * 3
    return 9 * ands + 100 * hundredsstr + zero2ninetynine * 10 + len(list(
        'onethousand'))


def problem20():
    from operator import mul

    def fact(n):
        return reduce(mul, xrange(2, n + 1))

    return sum(map(int, list(str(fact(100)))))


def problem22():
    data = open('names.txt').readlines()
    data = data[0].split('","')
    data[0] = data[0][1:]  # Fix quotes on first and last terms
    data[-1] = data[-1][:-1]
    data.sort()

    def namescore(name):
        score = 0
        for letter in name:
            score = score + ord(letter) - 64
        return score

    namescores = map(namescore, data)
    return sum([(i + 1) * namescores[i] for i in xrange(0, len(data))])


def problem24():
    """What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    from itertools import permutations

    n = '0123456789'
    perms = permutations(n)
    for perm in enumerate(perms):
        if perm[0] == 1000000 - 1:  # Enumerate is zero-indexed
            return int(''.join(perm[1]))


def problem25():
    fibs = [1, 1]
    n = 2
    while len(list(str(fibs[-1]))) < 1000:
        fibs.append(fibs[n - 2] + fibs[n - 1])
        n = n + 1
    return n

def problem30():
    """Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.

    Caches exponentials in fifth_pow array to save time. """
    fifth_pow = [0, 1 ** 5, 2 ** 5, 3 ** 5, 4 ** 5, 5 ** 5, 6 ** 5, 7 ** 5, 8 ** 5, 9 ** 5]

    def fifth(x):
        return fifth_pow[x]

    winners = []
    for i in xrange(2, 300000):
        digit_list = map(int, list(str(i)))
        summ = sum(map(fifth, digit_list))
        print str(i).ljust(15), str(summ).ljust(15), i - summ
        if i == summ:
            winners.append(i)

    return sum(winners)

# def problem