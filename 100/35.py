import numpy as np

A = np.random.random(3)
B = np.random.random(3)

print (A)
print (B)
np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)

print('the solution for the two matrices are', A)
