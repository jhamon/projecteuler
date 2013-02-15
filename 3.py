# What is the largest prime factor of the number 600851475143 ?
#  We only need to check factors up to sqrt(n)


def check_max(n):
    n = max(n)
    i = int(n ** 0.5)
    while True:
        if n % i == 0:
            return (i, n / i)
        elif i == 1:
            i = i - 1
            break
        i = i - 1
    return (n, 1)


def recur_check(n):
    while not 1 in n:
        n = check_max(n)
        # print n
    prime_factors.append(max(n))
    return n

a = 600851475143
prime_factors = [1]
start = a / max(prime_factors)
while True:
    next = check_max((1, start))
    next2 = recur_check(next)
    start = start / max(next2)
    if max(next2) == max(next):
        print 'answer:', max(next2)
        print 'factors:', prime_factors
        break
