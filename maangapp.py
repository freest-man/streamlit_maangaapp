# Import necessary libraries
import yfinance as yf
import streamlit as st
import pandas as pd

# Sidebar for user input features
st.sidebar.header('Select Stock')

def get_user_selected_stock():
    selected_stock = st.sidebar.selectbox('Choose Stock', ('GOOGL', 'AAPL', 'AMZN', 'NFLX', 'META'))
    return selected_stock

# Get user input
ticker_symbol = get_user_selected_stock()

# Display selected stock information
st.write(f"Displaying historical data for {ticker_symbol} stock:")
st.write("Closing price and volume trends:")

# Get data on the selected ticker
ticker_data = yf.Ticker(ticker_symbol)

# Get historical trends for the selected ticker
historical_data = ticker_data.history(period='1d', start='2010-5-31', end='2024-1-1')

# Display closing price trends
st.write("## Closing Price")
st.line_chart(historical_data.Close)

# Display volume trends
st.write("## Volume")
st.line_chart(historical_data.Volume)

