import pandas as pd
import numpy as np

df = pd.read_csv('pokemon.csv')

df.head(3)

df['sum'] = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(1)

df['result'] = np.where(df['sum']==df['Total'],'same','different')

if(df['result'].nunique() > 1):
    print("校验错误")
else:
    print("校验成功")

df_drop = df.drop_duplicates('#', keep='first')
print("共有" + str(df_drop['Type 1'].nunique()) + "种")

print("前三多的为" + str(df_drop['Type 1'].value_counts().index[:3]))

df_doubledrop = df_drop.drop_duplicates(['Type 1', 'Type 2'])
print("共有" + str(df_doubledrop.shape[0]) + "种")

ls1 = list(set(df_drop['Type 1']))
df_dropna = df_drop.dropna(subset = 'Type 2')
ls2 = list(set(df_dropna['Type 2']))
ls2 = [i for i in ls2 if i != '']
print(ls2)

data1 = {
    "Type 1" : ls1
}
data2 = {
    "Type 2" : ls2
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df1['value']=1
df2['value']=1

df3 = df1.merge(df2,how='left',on='value')

print(type(df3))
print("共有" + str(df3.shape[0]-df_doubledrop.shape[0]) + "种未出现")

print(df['Attack'].mask(df['Attack']>120, 'high'
                 ).mask(df['Attack']<50, 'low').mask((50<=df['Attack']
                 )&(df['Attack']<=120), 'mid'))

print(df['Type 1'].replace({i:str.upper(i) for i in df['Type 1'
            ].unique()}))

print(df['Type 1'].apply(lambda x:str.upper(x)))

df['Deviation'] = df[['HP', 'Attack', 'Defense', 'Sp. Atk',
                     'Sp. Def', 'Speed']].apply(lambda x:np.max(
                     (x-x.median()).abs()), 1)
print(df.sort_values('Deviation', ascending=False).head())