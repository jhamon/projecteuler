from __future__ import division
from operator import mul
# This problem asks us to find the least common multiple
# of all numbers less than 20.


divisors = [2, 3, 5, 7, 9, 11, 13, 17, 19]


def prime_tree(n):
    dividend = n
    factors = []
    i = 0
    while True:
        divisor = divisors[i]
        quotient = dividend / divisor
        if int(quotient) == quotient:
            factors.append(divisor)
            dividend = quotient
        elif int(quotient) != quotient:
            i = i + 1
        if quotient == 1:
            break
    return factors

# List of lists containing the factors of each number up to 20
factorlist = [prime_tree(i) for i in range(2, 21)]

# Count number of times each factor occurs in each list
countexp = [map(x.count, divisors) for x in factorlist]

# Find the exponent for each prime term
exponents = map(max, [[countexp[i][j] for i in range(
    0, len(countexp))] for j in range(0, len(divisors))])

# Now put everything together again
lcm = reduce(
    mul, [divisors[i] ** exponents[i] for i in range(0, len(divisors))], 1)

print lcm
