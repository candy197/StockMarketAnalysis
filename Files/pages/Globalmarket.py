import streamlit as st
import yfinance as yf
import nsepy as nse
import pandas as pd

st.set_page_config(page_title="Global Market",page_icon=":globe_with_meridians:",layout="wide")
st.title('Welcome To Global Market Research Playground :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

indice = pd.read_csv("pages/MarketIndice.csv")


option = st.selectbox('Which indice you like to trade?',(indice))
#Fetch like (Low, High,Priviously Closed,R)




