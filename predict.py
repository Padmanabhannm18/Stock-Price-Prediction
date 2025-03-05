import numpy as np
import streamlit as st

def predict_stock_price(model, scaler, input_features):
    """Predicts stock price based on user input."""
    scaled_data = scaler.transform([input_features])
    prediction = model.predict(scaled_data)
    return prediction[0]
