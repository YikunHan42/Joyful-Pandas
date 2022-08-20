import numpy as np

f = lambda x:np.diff(np.nonzero(np.r_[1,np.diff(x)!=1,1])).max()