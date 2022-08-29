import pandas as pd

df = pd.read_csv('chocolate.csv')

df.columns = [' '.join(i.split('\n')) for i in df.columns]

df.head(3)

df['Cocoa Percent'] = df['Cocoa Percent'].apply(lambda x:float(x[:-1])/100)

df.query('(Rating<3)&(`Cocoa Percent`>`Cocoa Percent`.median())').head(3)

idx = pd.IndexSlice

exclude = ['France', 'Canada', 'Amsterdam', 'Belgium']

res = df.set_index(['Review Date', 'Company Location']).sort_index(level=0)

res.loc[idx[2012:,~res.index.get_level_values(1).isin(exclude)],:].head(3)