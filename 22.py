
data = open('names.txt').readlines()
data = data[0].split('","')
print data[0], data[-1]
data[0] = data[0][1:] # Fix quotes on first and last terms
data[-1] = data[-1][:-1]
print data[0], data[-1]
data.sort()

def namescore(name):
	score = 0
	for letter in name:
		score = score + ord(letter) - 64
	return score

namescores = map(namescore,data)
print sum([(i+1)*namescores[i] for i in xrange(0,len(data))])
