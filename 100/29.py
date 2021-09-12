import numpy as np

Z = np.random.uniform(-10,+10,10)
print(np.where(Z>0, np.ceil(Z), np.floor(Z)))
