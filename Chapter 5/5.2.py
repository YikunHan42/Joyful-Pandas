import pandas as pd

df = pd.DataFrame({'Class':[1,2],
                  'Name':['San Zhang', 'Si Li'],
                  'Chinese':[80, 90],
                  'Math':[80, 75]})

print(df)

df = df.rename(columns={'Chinese':'pre_Chinese', 'Math':'pre_Math'})

pd.wide_to_long(df,
                stubnames=['pre'],
                i = ['Class', 'Name'],
                j='Subject',
                sep='_',
                suffix='.+').reset_index().rename(columns={'pre':'Grade'})

