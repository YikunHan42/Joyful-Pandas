import numpy as np

np.random.seed(0)

m, n, p = 100, 80, 50

B = np.random.randint(0, 2, (m, p))

U = np.random.randint(0, 2, (p, n))

Z = np.random.randint(0, 2, (m, n))

(((B**2).sum(1).reshape(-1,1) + (U**2).sum(0) - 2*B@U)*Z).sum()