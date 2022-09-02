import pandas as pd

import numpy as np

class my_groupby:
    def __init__(self, my_df, group_cols):
        self.my_df = my_df.copy()
        self.groups = my_df[group_cols].drop_duplicates()
        if isinstance(self.groups, pd.Series):
            self.groups = self.groups.to_frame()
        self.group_cols = self.groups.columns.tolist()
        self.groups = {i: self.groups[i].values.tolist(
                       ) for i in self.groups.columns}
        self.transform_col = None
    def __getitem__(self, col):
        self.pr_col = [col] if isinstance(col, str) else list(col)
        return self
    def transform(self, my_func):
        self.num = len(self.groups[self.group_cols[0]])
        L_order, L_value = np.array([]), np.array([])
        for i in range(self.num):
            group_df = self.my_df.reset_index().copy()
            for col in self.group_cols:
                group_df = group_df[group_df[col]==self.groups[col][i]]
            group_df = group_df[self.pr_col]
            if group_df.shape[1] == 1:
                group_df = group_df.iloc[:, 0]
            group_res = my_func(group_df)
            if not isinstance(group_res, pd.Series):
                group_res = pd.Series(group_res,
                                      index=group_df.index,
                                      name=group_df.name)
            L_order = np.r_[L_order, group_res.index]
            L_value = np.r_[L_value, group_res.values]
        self.res = pd.Series(pd.Series(L_value, index=L_order).sort_index(
                   ).values,index=self.my_df.reset_index(
                   ).index, name=my_func.__name__)
        return self.res


my_groupby(df, 'Type')

def f(s):
    res = (s-s.min())/(s.max()-s.min())
    return res


my_groupby(df, 'Type')['Price'].transform(f).head()

df.groupby('Type')['Price'].transform(f).head()

my_groupby(df, ['Type','Country'])['Price'].transform(f).head()

df.groupby(['Type','Country'])['Price'].transform(f).head()

my_groupby(df, 'Type')['Price'].transform(lambda x:x.mean()).head()

df.groupby('Type')['Price'].transform(lambda x:x.mean()).head()

my_groupby(df, 'Type')['Disp.', 'HP'].transform(
               lambda x: x['Disp.']/x.HP).head()
