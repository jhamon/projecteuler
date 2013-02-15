def square(x):
	return x**2

sumofsquares = sum(map(square,xrange(1,101)))
squareofsum = square(sum(xrange(1,101)))

print (squareofsum - sumofsquares)