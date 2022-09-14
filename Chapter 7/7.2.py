import pandas as pd

from sklearn.neighbors import KNeighborsRegressor

df = pd.read_excel('data/color.xlsx')

df_dummies = pd.get_dummies(df.Color)

stack_list = []

for col in df_dummies.columns:
    clf = KNeighborsRegressor(n_neighbors=6)
    clf.fit(df.iloc[:,:2].values, df_dummies[col].values)
    res = clf.predict([[0.8, -0.2]]).reshape(-1,1)
    stack_list.append(res)


code_res = pd.Series(np.hstack(stack_list).argmax(1))

print(df_dummies.columns[code_res[0]])

from sklearn.neighbors import KNeighborsRegressor

df = pd.read_csv('data/audit.csv')

res_df = df.copy()

df = pd.concat([pd.get_dummies(df[['Marital', 'Gender']]),
    df[['Age','Income','Hours']].apply(
        lambda x:(x-x.min())/(x.max()-x.min())), df.Employment],1)


X_train = df.query('Employment.notna()')

X_test = df.query('Employment.isna()')

df_dummies = pd.get_dummies(X_train.Employment)

stack_list = []

for col in df_dummies.columns:
    clf = KNeighborsRegressor(n_neighbors=6)
    clf.fit(X_train.iloc[:,:-1].values, df_dummies[col].values)
    res = clf.predict(X_test.iloc[:,:-1].values).reshape(-1,1)
    stack_list.append(res)


code_res = pd.Series(np.hstack(stack_list).argmax(1))

cat_res = code_res.replace(dict(zip(list(
            range(df_dummies.shape[0])),df_dummies.columns)))


res_df.loc[res_df.Employment.isna(), 'Employment'] = cat_res.values

print(res_df.isna().sum())