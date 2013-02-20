def problem2():
	""" Returns the sum of all fibonacci numbers less than 4 million"""
	fibs = [1, 1]
	while fibs[-1] < 4000000:
		fibs.append(fibs[-1]+fibs[-2])
	fibs = fibs[:-1]

	return sum([x for x in fibs if x%2==0])
