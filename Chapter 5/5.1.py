import pandas as pd

df = pd.read_csv('drugs.csv').sort_values([
     'State','COUNTY','SubstanceName'],ignore_index=True)

print(df.head(3))

df1 = df.copy()

df1 = df1.pivot(index=['State','COUNTY','SubstanceName'
              ], columns='YYYY', values='DrugReports'
              ).reset_index().rename_axis(columns={'YYYY':''})


print(df1.head(3))

df2 = df.melt(id_vars = ['State','COUNTY','SubstanceName'],
                     value_vars = df1.columns[-8:],
                     var_name = 'YYYY',
                     value_name = 'DrugReports').dropna(
                     subset=['DrugReports'])


df2= df2[df.columns].sort_values([
              'State','COUNTY','SubstanceName'],ignore_index=True
              ).astype({'YYYY':'int64', 'DrugReports':'int64'})

print(df2.equals(df))

df3 = df.pivot_table(index='YYYY', columns='State',
                     values='DrugReports', aggfunc='sum')


print(df3.head(3))

df3 = df.groupby(['State', 'YYYY'])['DrugReports'].sum(
                ).to_frame().unstack(0).droplevel(0,axis=1)


print(df3.head(3))


