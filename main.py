import streamlit as st
import yfinance as yf
from nsetools import Nse
from st_pages import Page,show_pages
import nsepy as Np
st.title(':rainbow[Welcome To Trading World] :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')


show_pages(
    [
        Page("main.py","Home","🏠"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Equity.py","Equity Research",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Globalmarket.py","Global Market",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/MF.py","Mutual Fund Research",":books:"),
        Page("C:/Users/UnknownMan/Desktop/StockMarketAnalysis/pages/Options.py","Options Trading Research",":books:")

    ]
)