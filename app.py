import streamlit as st
import yfinance as yf
import datetime

st.write("""
         # Stock Price Analyser
         """)

#get data for Apple's stocks - yfinance has Apple symple as AAPL
#symbol = "AAPL"

#give a select box to get input from user to select from diffrent stocks to analyse
symbol = st.selectbox("Which stock do you want to analyse", ("AAPL", "TSLA", "MSFT"))

col1, col2 = st.columns(2)

#Take input as date from user using widgets
with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2019, 7, 6))

with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2019, 7, 10))

ticker_data = yf.Ticker(symbol)

# to get daily data from start to end date
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

# use formatterdstring symbols as per user input 
st.write(f"""
         ### {symbol}'s stock price data """)
st.dataframe(ticker_df)

st.write(f"""
         ### {symbol}'s closing price chart""")
st.line_chart(ticker_df["Close"])


st.write(f"""
         ### {symbol}'s volume  chart""")
st.line_chart(ticker_df["Volume"])



