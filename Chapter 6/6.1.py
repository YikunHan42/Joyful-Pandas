import pandas as pd

date = pd.date_range('20200412', '20201116').to_series()

date = date.dt.month.astype('string').str.zfill(2
       ) +'-'+ date.dt.day.astype('string'
       ).str.zfill(2) +'-'+ '2020'


date = date.tolist()


L = []


for d in date:
    df = pd.read_csv('data/us_report/' + d + '.csv', index_col='Province_State')
    data = df.loc['New York', ['Confirmed','Deaths',
                  'Recovered','Active']]
    L.append(data.to_frame().T)


res = pd.concat(L)

res.index = date

res.head()