#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
import altair as alt
import pandas as pd


# In[5]:


data = yf.download('IXI.L', period='5y')


# In[8]:


data.loc[pd.datetime(2019, 12, 18)].Close


# In[7]:


price = alt.Chart(data.reset_index()).mark_line().encode(
x = 'Date:T',
y = 'Close',
tooltip=['Date', 'Open', 'Close', 'High', 'Low', 'Volume'],
).properties(width=600, height=200)

volume = alt.Chart(data.reset_index()).mark_line().encode(
x = 'yearmonth(Date):T',
y = 'mean(Volume)').properties(width = 600, height = 200)

price & volume


# In[ ]:




