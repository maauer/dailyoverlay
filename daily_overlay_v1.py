# -*- coding: utf-8 -*-
"""Daily Overlay v1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NbUMtaRPLKH0DkFOftF_EsFoa_3K-tTe
"""

!pip install yfinance mplfinance
import yfinance as yf
import mplfinance as mpf

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime as datetime
from datetime import date 
from datetime import timedelta

aig = yf.Ticker("YNDX")
aigh = aig.history(period="1d", interval="1m")
df = pd.DataFrame(aigh)
yester = date.today() - timedelta(days = 3)
yesterr = date.today() - timedelta(days = 2)
aigh2 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
df2 = pd.DataFrame(aigh2)
#-------------------
yester = date.today() - timedelta(days = 4)
yesterr = date.today() - timedelta(days = 3)
aigh3 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dff2 = pd.DataFrame(aigh3)
yester = date.today() - timedelta(days = 5)
yesterr = date.today() - timedelta(days = 4)
aigh4 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dfg2 = pd.DataFrame(aigh4)
yester = date.today() - timedelta(days = 6)
yesterr = date.today() - timedelta(days = 5)
aigh5 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dgf2 = pd.DataFrame(aigh5)

yester = date.today() - timedelta(days = 9)
yesterr = date.today() - timedelta(days = 8)
aighh2 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
df22 = pd.DataFrame(aighh2)
yester = date.today() - timedelta(days = 10)
yesterr = date.today() - timedelta(days = 9)
aighh3 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dff22 = pd.DataFrame(aighh3)
yester = date.today() - timedelta(days = 11)
yesterr = date.today() - timedelta(days = 10)
aighh4 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dfg22 = pd.DataFrame(aighh4)
yester = date.today() - timedelta(days = 12)
yesterr = date.today() - timedelta(days = 11)
aighh5 = aig.history(start = yester, end=yesterr, interval="1m", actions=False)
dgf22 = pd.DataFrame(aighh5)

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()

fig = go.Figure(data=[go.Candlestick(x=df2.index,
                open=df2['Open'],
                high=df2['High'],
                low=df2['Low'],
                close=df2['Close'])])

fig.show()

dat = [go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']), 
       go.Candlestick(x=df.index, open=df2['Open'], high=df2['High'], low=df2['Low'], close=df2['Close']),
       go.Candlestick(x=df.index, open=dff2['Open'], high=dff2['High'], low=dff2['Low'], close=dff2['Close']),
       go.Candlestick(x=df.index, open=dgf2['Open'], high=dgf2['High'], low=dgf2['Low'], close=dgf2['Close']),
       go.Candlestick(x=df.index, open=dfg2['Open'], high=dfg2['High'], low=dfg2['Low'], close=dfg2['Close']),
       go.Candlestick(x=df.index, open=df22['Open'], high=df22['High'], low=dff22['Low'], close=df22['Close']),
       go.Candlestick(x=df.index, open=dff22['Open'], high=dff22['High'], low=dff2['Low'], close=dff22['Close']),
       go.Candlestick(x=df.index, open=dgf22['Open'], high=dgf22['High'], low=dgf22['Low'], close=dgf22['Close']),
       go.Candlestick(x=df.index, open=dfg22['Open'], high=dfg22['High'], low=dfg22['Low'], close=dfg22['Close']) ]
fig = go.Figure(data=dat)

fig.show()