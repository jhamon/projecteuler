def square(x):
	return x**2

sumofsquares = sum(map(square,range(1,101)))
squareofsum = square(sum(range(1,101)))

print (squareofsum - sumofsquares)