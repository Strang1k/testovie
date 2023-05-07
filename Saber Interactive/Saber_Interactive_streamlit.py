import streamlit as st
import numpy as np
from pandas import DataFrame
from requests import get
import datetime
#import matplotlib.pyplot as plt


st.set_page_config(layout='centered', initial_sidebar_state='expanded')
keyv = {'BTC':'bitcoin', 'ETH':'ethereum', 'SOBAKA':'dogecoin'}

сurrency = st.sidebar.selectbox("Select an asset: ", ['BTC', 'ETH', 'SOBAKA'])
сurrency = keyv[сurrency]
#data_interval = st.sidebar.selectbox("Select an asset: ", ['d1', 'm1', 'm5', 'm15', 'm30', 'h1', 'h2','h6', 'h12'])


#способ добавить два селектора в одну строку
layout = st.sidebar.columns([1, 1]) 
with layout[0]: 
    date_from = st.date_input('Date from', datetime.date(2022, 12, 10))
with layout[-1]: 
    date_to = st.date_input('Date to', datetime.date(2023, 1, 10))

#разработчики работают над возможностью изменить представление даты,
#но ее пока что нет, и доступен только yyyy-mm-dd формат
#https://github.com/streamlit/streamlit/issues/5234


#перевод в требуемый api формат времени
date_from = int(datetime.datetime.combine(date_from, datetime.time.min).timestamp()*1000)
date_to = int(datetime.datetime.combine(date_to, datetime.time.max).timestamp()*1000)

#формируем ссылку и получаем данные
url = f'https://api.coincap.io/v2/assets/{сurrency}/history?interval=d1&start={date_from}&end={date_to}'
data = get(url).json()

#парсим цену и дату
price = []
date = []
for i in range (len(data['data'])):
    temp = data['data'][i]
    price.append( round(float( temp['priceUsd']), 4) )
    date.append(temp['date'][:10])

#исп встроенный bar_chart
df = DataFrame({'date':date, 'price':price})
st.bar_chart(df, x= 'date', y= 'price')


#plt график
# fig = plt.figure() 
# plt.bar(date, price) 
# st.pyplot(fig)