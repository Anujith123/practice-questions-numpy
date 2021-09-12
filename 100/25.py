import numpy as np


Z = np.arange(11)
Z[(3 < Z) & (Z < 8)] *= -1
print(Z)
