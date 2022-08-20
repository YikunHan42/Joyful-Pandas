import numpy as np

A = np.arange(1,10).reshape(3,-1)

B = A*(1/A).sum(1).reshape(-1,1)

print(B)