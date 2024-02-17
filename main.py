import streamlit as st
import yfinance as yf
from st_pages import Page,show_pages
import nsepy as Np
import pandas as pd 
import sqlite3 as sql
from bs4 import BeautifulSoup
import requests as rt
import os 
from newsapi.newsapi_client import NewsApiClient
import newsapi 



st.set_page_config(page_title="Home",page_icon=":bar_chart:",layout="wide")
st.title('Market News and Trends :sunglasses:')
st.header("", divider="rainbow")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
Path = os.getcwd()+"/pages/"
show_pages(
    [
        Page("main.py","Home","🏠"),
        Page(Path+"Equity.py","Equity Research",":books:"),
        Page(Path+"Globalmarket.py","Global Market",":books:"),
        Page(Path+"MF.py","Mutual Fund Research",":books:"),
        Page(Path+"Options.py","Options Trading Research",":books:")

    ]
)
indice = pd.read_csv("pages/MarketIndice.csv")
col1=st.columns(1)

with col1:
    st.header("Nifty Index")
    option = st.selectbox(
    'Which index you want to Select?',indice)
    st.write('You selected:', option)




#Offline Data Processing


def ConnectionCheck():
    try:
        response = rt.get("https://www.moneycontrol.com", timeout=5)
        return True
    except rt.ConnectionError:
        return False    
if ConnectionCheck() == True:
        print("We Can Proccess With online.")
else:
    print("Internet is not connected we can still work on Offline data.")