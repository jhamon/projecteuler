# Find a pythagorean triple with a+b+c = 1000

# a**2 + b**2 == c**2
# therefore, a**2 == c**2 - b**2
# a**2 = (c-b)(c+b)
#   P.S. I now see the solution is just 25x 8-15-17 triangle. Lame.

from itertools import permutations
from math import sqrt
b = xrange(1,500)
perms = permutations(b,2)
for p in perms:
	if p[1] > p[0]:
		B, C = p[0], p[1]
		diffsq = (C-B)*(C+B)
		sqrtdiffsq = sqrt(diffsq)
		if sqrtdiffsq+B+C == 1000:
			print sqrtdiffsq*B*C
			break

