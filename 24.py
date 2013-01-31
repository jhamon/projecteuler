from itertools import permutations

n = '0123456789'
perms = permutations(n)
for perm in enumerate(perms):
	if perm[0] == 1000000-1: # Enumerate is zero-indexed
		print ''.join(perm[1])
		break
