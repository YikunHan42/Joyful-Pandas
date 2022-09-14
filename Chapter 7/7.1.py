import pandas as pd

df = pd.read_csv('missing_chi.csv')

cat_1 = df.X_1.fillna('NaN').mask(df.X_1.notna()).fillna("NotNaN")

cat_2 = df.X_2.fillna('NaN').mask(df.X_2.notna()).fillna("NotNaN")

df_1 = pd.crosstab(cat_1, df.y, margins=True)

df_2 = pd.crosstab(cat_2, df.y, margins=True)

def compute_S(my_df):
    S = []
    for i in range(2):
        for j in range(2):
            E = my_df.iat[i, j]
            F = my_df.iat[i, 2]*my_df.iat[2, j]/my_df.iat[2,2]
            S.append((E-F)**2/F)
    return sum(S)


res1 = compute_S(df_1)

res2 = compute_S(df_2)