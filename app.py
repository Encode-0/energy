import requests
import datetime
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import date, timedelta

txt = 'Token ' + str(st.secrets.DB_TOKEN)
days == 1
dt_obj = date.today() - timedelta(days=days)
dt = str(dt_obj)
tup = (str(dt_obj.day), str(dt_obj.month), str(dt_obj.year))
dt_trans = '-'.join(tup)

try:   
    url = f'https://data.gov.gr/api/v1/query/admie_dailyenergybalanceanalysis?date_from={dt}&date_to={dt}'
    headers = {'Authorization': txt}
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
    plt.title('Ενεργειακό Ισοζύγιο στις ' + dt_trans, bbox={'facecolor':'0.8', 'pad':5})
    plt.pie(df.percentage,
        labels=df.fuel,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True);

    st.pyplot(fig)
    
except:
  
    days += 1
    
    dt_obj = date.today() - timedelta(days=days)

    dt = str(dt_obj)
    tup = (str(dt_obj.day), str(dt_obj.month), str(dt_obj.year))
    dt_trans = '-'.join(tup)
    
    url = f'https://data.gov.gr/api/v1/query/admie_dailyenergybalanceanalysis?date_from={dt}&date_to={dt}'
    headers = {'Authorization': txt}
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
    plt.title('Ενεργειακό Ισοζύγιο στις ' + dt_trans, bbox={'facecolor':'0.8', 'pad':5})
    plt.pie(df.percentage,
        labels=df.fuel,
        explode=explode,
        autopct='%1.1f%%',
        shadow=True);

    st.pyplot(fig)
