import numpy as np

data = np.loadtxt('13.dat')
bigsum = sum(data)
print ''.join(str(bigsum)[0:11].split('.'))