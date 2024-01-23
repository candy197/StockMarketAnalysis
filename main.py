import streamlit as st
import yfinance as yf
from st_pages import Page,show_pages
import nsepy as Np
import pandas as pd 
import sqlite3 as sql
from bs4 import BeautifulSoup
import requests as rt



st.set_page_config(page_title="Home",page_icon=":bar_chart:",layout="wide")
st.title('Welcome To Candy Trading World :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)


def dataPull():
    pass



dataRender = pd.read_html("https://www.moneycontrol.com/india/stockmarket/sector-classification/marketstatistics/nse/agri.html")




show_pages(
    [
        Page("main.py","Home","🏠"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Equity.py","Equity Research",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Globalmarket.py","Global Market",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/MF.py","Mutual Fund Research",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Options.py","Options Trading Research",":books:")

    ]
)

