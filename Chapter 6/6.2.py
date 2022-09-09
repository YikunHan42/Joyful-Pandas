import pandas as pd
import numpy as np

def join(df1, df2, how='left'):
    res_col = df1.columns.tolist() +  df2.columns.tolist()
    dup = df1.index.unique().intersection(df2.index.unique())
    res_df = pd.DataFrame(columns = res_col)
    for label in dup:
        cartesian = [list(i)+list(j) for i in df1.loc[label
                    ].values.reshape(-1,1) for j in df2.loc[
                      label].values.reshape(-1,1)]
        dup_df = pd.DataFrame(cartesian, index = [label]*len(
                 cartesian), columns = res_col)
        res_df = pd.concat([res_df,dup_df])
    if how in ['left', 'outer']:
        for label in df1.index.unique().difference(dup):
            if isinstance(df1.loc[label], pd.DataFrame):
                cat = [list(i)+[np.nan]*df2.shape[1
                      ] for i in df1.loc[label].values]
            else: cat = [list(i)+[np.nan]*df2.shape[1
                      ] for i in df1.loc[label].to_frame().values]
            dup_df = pd.DataFrame(cat, index = [label
                      ]*len(cat), columns = res_col)
            res_df = pd.concat([res_df,dup_df])
    if how in ['right', 'outer']:
        for label in df2.index.unique().difference(dup):
            if isinstance(df2.loc[label], pd.DataFrame):
                cat = [[np.nan]+list(i)*df1.shape[1
                      ] for i in df2.loc[label].values]
            else: cat = [[np.nan]+list(i)*df1.shape[1
                      ] for i in df2.loc[label].to_frame().values]
            dup_df = pd.DataFrame(cat, index = [label
                      ]*len(cat), columns = res_col)
            res_df = pd.concat([res_df,dup_df])
    return res_df


df1 = pd.DataFrame({'col1':[1,2,3,4,5]}, index=list('AABCD'))

print(df1)

df2 = pd.DataFrame({'col2':list('opqrst')}, index=list('ABBCEE'))

print(df2)

print(join(df1, df2, how='outer'))
