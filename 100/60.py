import numpy as np

Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())
