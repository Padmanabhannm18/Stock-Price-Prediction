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
    historical_data = stock.history(period="1y")
    todays_data = stock.history(period="1d", interval="1m")
    company_name = stock.info.get("longName", "Unknown Company")

    st.write(f"### {company_name} ({ticker})")
    if not historical_data.empty:
        last_updated_historical = historical_data.index[-1].strftime("%Y-%m-%d")
        st.write(f"**Last historical update:** {last_updated_historical}")
    else:
        st.write("No historical data available.")

    if not todays_data.empty:
        last_updated_today = todays_data.index[-1].strftime("%Y-%m-%d %H:%M:%S")
        latest_price = todays_data["Close"].iloc[-1]  # Latest price of today
        st.write(f"**Last updated today:** {last_updated_today}")
        st.write(f"**Latest price:** ${latest_price:.2f}")
    else:
        st.write("No data available for today.")

    return historical_data, todays_data

