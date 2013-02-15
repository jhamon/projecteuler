import numpy as np
from operator import mul

data = np.loadtxt('11.txt')

print data[0,0]
print data.shape

# vertical
print max([reduce(mul, data[i:i+4,j]) for i in xrange(0,20-3) for j in xrange(0,20)])

# horizontal
print max([reduce(mul, data[i,j:j+4]) for i in xrange(0,20) for j in xrange(0,20-3)])

# Diagonal 1
print max([reduce(mul,[data[i,j], data[i+1,j+1], data[i+2,j+2], data[i+3,j+3]]) for i in xrange(0,17) for j in xrange(0,17)])

# Diagonal 2
print max([reduce(mul,[data[i,j], data[i-1,j-1], data[i-2,j-2], data[i-3,j-3]]) for i in xrange(0,17) for j in xrange(0,17)])
for i in [[data[i,j], data[i-j,j-1], data[i-2,j-2], data[i-3,j-3]] for i in xrange(0,17) for j in xrange(0,17)]:
	print i