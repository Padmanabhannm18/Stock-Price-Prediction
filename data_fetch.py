import yfinance as yf
import pandas as pd

def get_realtime_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # Fetch last 30 days data
        if not data.empty:
            return data
        else:
            return pd.DataFrame()
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return pd.DataFrame()
