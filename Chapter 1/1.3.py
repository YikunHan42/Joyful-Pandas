import numpy as np

np.random.seed(0)

A = np.random.randint(10, 20, (8, 5))

B = A.sum(0)*A.sum(1).reshape(-1, 1)/A.sum()

res = ((A-B)**2/B).sum()

res