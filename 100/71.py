import numpy as np
A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print(A * B[:,:,None])
