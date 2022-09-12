import requests
import datetime
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import date, timedelta

datetime_obj = date.today() - timedelta(days=1)
yesterday = str(datetime_obj)
tup = (str(datetime_obj.day), str(datetime_obj.month), str(datetime_obj.year))
d = '-'.join(tup)

url = f'https://data.gov.gr/api/v1/query/admie_dailyenergybalanceanalysis?date_from={yesterday}&date_to={yesterday}'
headers = {'Authorization': 'Token 0dbb7978c0c26221814f2ac382c3674801fdf83a'}
response = requests.get(url, headers=headers)
df = pd.DataFrame.from_dict(response.json(),
                            orient='columns',
                            dtype=None,
                            columns=None)

df.drop(df[df.fuel == 'ΣΥΝΟΛΟ'].index, inplace = True)

explode = [0, 0, 0, 0, 0]
explode[df.percentage.argmax()] = 0.1
explode = tuple(explode)

fig, ax = plt.subplots(figsize=(12, 12))
fig.subplots_adjust(0.3,0,1,1)
plt.title('Ενεργειακό Ισοζύγιο στις ' + d, bbox={'facecolor':'0.8', 'pad':5})
plt.pie(df.percentage,
        labels=df.fuel,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True);

st.pyplot(fig)
