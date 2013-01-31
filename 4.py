# Largest palindrome formed as product of two 3-digit numbers

a = range(1000,900,-1)
b = a
pals = []
for factor1 in a:
	for factor2 in b:
		prod = factor2*factor1
		if str(prod)[::-1] == str(prod):
			pals.append(prod)
print max(pals)
