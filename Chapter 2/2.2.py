import pandas as pd
import numpy as np

np.random.seed(0)

s = pd.Series(np.random.randint(-1,2,30).cumsum())

s.ewm(alpha=0.2).mean().head()

def ewm_func(x, alpha=0.2):
    win = (1-alpha)**np.arange(x.shape[0])[::-1]
    res = (win*x).sum()/win.sum()
    return res


s.expanding().apply(ewm_func).head()

s.rolling(window=4).apply(ewm_func).head()