import numpy as np
A = np.random.uniform(0,1,(5,5))
B = np.random.uniform(0,1,(5,5))
np.sum(A * B.T, axis=1)