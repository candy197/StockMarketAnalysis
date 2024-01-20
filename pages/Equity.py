import streamlit as st
import yfinance as yf
import nsepy as nse


st.title(':rainbow[Welcome To Equity Research Playground] :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')


Cat_list = []


option = st.selectbox(
    'Which Sector you like to trade?',
    (Cat_list))
#Fetch like (Low, High,Priviously Closed,R)

sectors_df = yf.download("SECTOR")







