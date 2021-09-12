import numpy as np
X = np.random.rand(5, 10)

Y = X - X.mean(axis=1, keepdims=True)

print(Y)
