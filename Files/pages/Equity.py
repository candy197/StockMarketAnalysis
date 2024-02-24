import streamlit as st
import nsepy as nse
import pandas as pd

st.set_page_config(page_title="Equity Research",page_icon=":money_with_wings:",layout="wide")
st.title('Welcome To Equity Research Playground :blue[Be Cool Trader] :sunglasses:')
st.header('Letz be billionaire Together', divider='rainbow')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

indice = pd.read_csv("pages/MarketIndice.csv")


option = st.selectbox(
    'How would you like to be contacted?',indice
   )
st.write('You selected:', option)




#Fetch like (Low, High,Priviously Closed,R)








