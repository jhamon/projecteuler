# Sum of all primes less than 2 million
from math import sqrt

primelist = [2,3]
i = 5
while primelist[-1]<2000000:
    upperbound = int(sqrt(i))+1 # Only check to sqrt(n)
    for j in range(2,upperbound+1):
        if i%j==0: # Divisible, so not prime
            break 
        if j == upperbound:
            primelist.append(i)
            break
    i = i + 2 # increment by 2, to check odds only


print 'sum: ', sum(primelist[:-1])