import streamlit as st
import yfinance as yf
from st_pages import Page,show_pages
import nsepy as Np
import pandas as pd 
import sqlite3 as sql
from bs4 import BeautifulSoup
import requests as rt
import os 



st.set_page_config(page_title="Home",page_icon=":bar_chart:",layout="wide")
st.title('Welcome To Candy Trading World :blue[Be Cool Trader] :sunglasses:')
st.header('Market News and Trends', divider='rainbow')
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



