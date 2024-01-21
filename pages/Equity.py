import streamlit as st
import yfinance as yf
import nsepy as nse
import pandas as pd


st.title(':rainbow[Welcome To Equity Research Playground] :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')

indice = pd.read_csv("pages/MarketIndice.csv")


option = st.selectbox('Which indice you like to trade?',(indice))
#Fetch like (Low, High,Priviously Closed,R)






