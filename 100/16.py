import numpy as np

Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


Z[:, [0, -1]] = 0
Z[[0, -1], :] = 0
print(Z)
