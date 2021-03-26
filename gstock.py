import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt

st.write("""

# Stock Price App

Shown are the stock price data for query companies

""")

#sidebar
st.sidebar.subheader('Stock Query')
startDate=st.sidebar.date_input("Start Date",dt.date(2020,1,1))
endDate=st.sidebar.date_input("End Date", dt.date(2021,3,25))



#getting the info of the ticker and storying it in a variable
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData=yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='Id',start=startDate,end=endDate)

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)
# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)
st.header(
 '**Closing Price**')
st.line_chart(tickerDf.Close)
st.header("**Volume**")
st.line_chart(tickerDf.Volume)
