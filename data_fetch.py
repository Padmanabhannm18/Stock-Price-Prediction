import yfinance as yf
import pandas as pd
import streamlit as st
def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(url)
    sp500_tickers = table[0]["Symbol"].tolist()
    return sp500_tickers

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    history = stock.history(period="1y")

    if not history.empty:
        last_updated = history.index[-1].strftime("%Y-%m-%d")
        st.write(f"Last updated date for {ticker}: {last_updated}")
    else:
        st.write(f"No data available for {ticker}")

    return history
