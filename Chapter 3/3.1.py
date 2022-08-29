import pandas as pd

df = pd.read_csv('company.csv')

dpt = ['Dairy', 'Bakery']

df.query("(age <= 40)&(department == @dpt)&(gender=='M')").head(3)

df.loc[(df.age<=40)&df.department.isin(dpt)&(df.gender=='M')].head(3)

df.iloc[(df.EmployeeID%2==1).values,[0,2,-2]].head()

df_op = df.copy()

df_op = df_op.set_index(df_op.columns[-3:].tolist()).swaplevel(0,2,axis=0)

df_op = df_op.reset_index(level=1)

df_op = df_op.rename_axis(index={'gender':'Gender'})

df_op.index = df_op.index.map(lambda x:'_'.join(x))

df_op.index = df_op.index.map(lambda x:tuple(x.split('_')))

df_op = df_op.rename_axis(index=['gender', 'department'])

df_op = df_op.reset_index().reindex(df.columns, axis=1)

df_op.equals(df)