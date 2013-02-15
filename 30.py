fifthpow = [0,1**5,2**5,3**5,4**5,5**5,6**5,7**5,8**5,9**5]

def fifth(x):
	return fifthpow[x]

winners = []
for i in xrange(2,300000):
	digit_list = map(int,list(str(i)))
	summ = sum(map(fifth,digit_list))
	print str(i).ljust(15), str(summ).ljust(15), i-summ
	if i == summ:
		winners.append(i)
		
print sum(winners)