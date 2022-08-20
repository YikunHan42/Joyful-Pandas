import numpy as np

M1 = np.random.rand(2,3)

M2 = np.random.rand(3,4)

res = [[sum([M1[i][k] * M2[k][j] for k in range(M1.shape[1])]) for j in range(M2.shape[1])] for i in range(M1.shape[0])]

print((np.abs((M1@M2 - res) < 1e-15)).all())