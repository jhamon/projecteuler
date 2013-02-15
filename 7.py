from math import sqrt
# The 10001st prime number

primelist = [2,3]
i = 5
while len(primelist)<10001:
    upperbound = int(sqrt(i))+1 # Only check to sqrt(n)
    for j in xrange(2,upperbound+1):
        if i%j==0: # Divisible, so not prime
            break 
        if j == upperbound:
            primelist.append(i)
            break
    i = i + 2 # increment by 2, to check odds only
print primelist[-1] # Answer!