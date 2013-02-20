def problem1():
	"""Print the sum of the numbers less than 1000 which are 
	   divisible by 3 or 5"""
	return sum([x for x in xrange(0,1000) if x%5==0 or x%3==0])
