import streamlit as st
import yfinance as yf
from st_pages import Page,show_pages
import nsepy as Np
import pandas as pd 
import sqlite3 as sql
from bs4 import BeautifulSoup
import requests as rt
import os 
from newsapi import NewsApiClient
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

col1,col2 = st.columns(2)
client = newsapi.NewsApiClient('dcd00510f4734ca680f217c72f668c80')

# Get top headlines
top_headlines = client.get_top_headlines(q="stock",
    category="business",
    language="en",
)

# Print the headlines
with col1:
    st.header("Market Top News")
for article in top_headlines["articles"]:
    with col1:
        with st.expander(article["title"]):
            st.write(article["description"])

with col2:
    st.header("Market Calender")


#Offline Data Processing


def ConnectionCheck():
    try:
        response = rt.get("https://dns.tutorialspoint.com", timeout=5)
        return True
    except rt.ConnectionError:
        return False    
if ConnectionCheck():
        print("We Can Proccess With online.")
else:
    print("Internet is not connected we can still work on Offline data.")