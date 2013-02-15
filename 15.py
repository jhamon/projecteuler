
from __future__ import division

n = 5
hist = [[1],[-1]]
for t in xrange(0,2*n):
	# print t
	for i in xrange(0,len(hist)):
		if hist[i].count(1) == n:
			hist[i] = hist[i] + [-1]
		elif hist[i].count(-1) == n:
			hist[i] = hist[i] + [1]
		else:
			hist.append(hist[i])
			hist[i] = hist[i] + [1]
			hist[-1] = hist[-1] + [-1]


# for item in hist:
	# print item

print 'goal: ', n, len(hist), len(hist)/(2**(2*n-1)-len(hist))