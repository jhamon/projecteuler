fibs = [1, 1]
n = 2
while len(list(str(fibs[-1]))) < 1000:
    fibs.append(fibs[n - 2] + fibs[n - 1])
    n = n + 1

print n