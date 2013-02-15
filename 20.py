from operator import mul

def fact(n):
	return reduce(mul,xrange(2,n+1))

print sum(map(int,list(str(fact(100)))))
