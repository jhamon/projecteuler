# Sum of even fibs < 4million

fibs = [1, 1]
while fibs[-1] < 4000000:
	fibs.append(fibs[-1]+fibs[-2])
fibs = fibs[:-1]

print sum([x for x in fibs if x%2==0])