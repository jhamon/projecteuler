from operator import mul

def fact(n):
	return reduce(mul,range(2,n+1))

print sum(map(int,list(str(fact(100)))))
