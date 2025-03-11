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

    # Get company name
    company_name = stock.info.get("longName", "Unknown Company")

    if not history.empty:
        last_updated = history.index[-1].strftime("%Y-%m-%d")
        st.write(f"Company: {company_name} ({ticker})")
        st.write(f"Last updated date: {last_updated}")
    else:
        st.write(f"No data available for {company_name} ({ticker})")

    return history
