import streamlit as st
from data_fetch import get_sp500_tickers,fetch_stock_data
from model import train_model, make_prediction
st.title("📈 Real-Time Stock Price Prediction")

sp500_tickers = get_sp500_tickers()

# Replace text input with a dropdown menu
ticker = st.sidebar.selectbox("Select a Stock Ticker", sp500_tickers)

if st.sidebar.button("Fetch Data"):
    st.write(f"Selected Stock: {ticker}")
    data = fetch_stock_data(ticker)
    if not data.empty:
        st.write(f"### {ticker} Stock Price Data (Last 1 year)")
        st.line_chart(data['Close'])
        st.dataframe(data['Close])
    else:
        st.error("Failed to fetch data. Please check the stock ticker.")

if st.sidebar.button("Train & Predict"):
    data = fetch_stock_data(ticker)
    if not data.empty:
        model, scaler = train_model(data)
        prediction = make_prediction(model, scaler, data)
        st.write(f"### Predicted Next Closing Price for {ticker}: **${prediction:.2f}**")
    else:
        st.error("Cannot train the model without data.")
