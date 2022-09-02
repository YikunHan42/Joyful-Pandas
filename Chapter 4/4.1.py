import pandas as pd

import numpy as np


df = pd.read_csv('data/car.csv')

df.head(3)

df.groupby('Country').filter(lambda x:x.shape[0]>2).groupby(
           'Country')['Price'].agg([(
           'CoV', lambda x: x.std()/x.mean()), 'mean', 'count'])

df.shape[0]

condition = ['Head']*20+['Mid']*20+['Tail']*20

df.groupby(condition)['Price'].mean()

res = df.groupby('Type').agg({'Price': ['max'], 'HP': ['min']})

res.columns = res.columns.map(lambda x:'_'.join(x))

def normalize(s):
    s_min, s_max = s.min(), s.max()
    res = (s - s_min)/(s_max - s_min)
    return res


df.groupby('Type')['HP'].transform(normalize).head()

df.groupby('Type')[['HP', 'Disp.']].apply(
   lambda x:np.corrcoef(x['HP'].values, x['Disp.'].values)[0,1])