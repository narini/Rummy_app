# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:05:31 2024

@author: natri

App der visualisere rummy excel arket 
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Funktioner #####

#funktion til at loade data
def load_data():
    data = pd.read_excel('Rummikub-2012.xlsm',None)
    return data 

def udtraek_point(year):
    data_year = data[year].iloc[2:].reset_index(drop=True)
    data_p = data_year[data_year.columns[9:]]
    #find hvor dataframe skal ende
    data_p_end_ix = data_p.columns[(data_p.values=='I alt').any(0)].to_list()[0]
    j = data_p.columns.get_loc(data_p_end_ix)
    data_p = data_p[data_p.columns[:j]]
    k = data_p[data_p.columns[0]]
    k = k[k.isnull()].index.min()
    data_p = data_p.loc[data_p.index[:k]]
    data_p = data_p.set_index(data_p.columns[0])#set første kolonne med navne som index
    return data_p

###     ##################
st.title('Rummikub mesterskaberne ')

data = load_data() #dictionary med faner fra alle år
years = list(data.keys())
# st.selectbox
st.write('Vælg årstal der skal analyseres')
year = st.selectbox('Vælg årstal', years)

### Figur med akumuleret point over spil ###
df = udtraek_point(year)
#flip dataframe for at have navne som kolonner
df = df.T
#fjerner første kolonne med 'Spil 1', 'Spil 2', etc.
df = df[df.columns[1:]].reset_index(drop=True)
st.dataframe(df)

fig = plt.figure()
plt.plot(df)
st.write(fig)
st.line_chart(df)
#Overvej at lave interaktiv figur med plotly

