import yfinance as yf

def get_sp500_tickers():
    import pandas as pd
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(url)
    sp500_tickers = table[0]["Symbol"].tolist()
    return sp500_tickers
