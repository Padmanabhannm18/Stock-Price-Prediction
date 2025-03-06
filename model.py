import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def train_model(data):
    data["Returns"] = data["Close"].pct_change()
    data.dropna(inplace=True)

    X = np.array(data["Returns"]).reshape(-1, 1)
    y = np.array(data["Close"])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, scaler

def make_prediction(model, scaler, data):
    latest_return = data["Returns"].iloc[-1]
    scaled_input = scaler.transform([[latest_return]])
    predicted_price = model.predict(scaled_input)[0]
    return predicted_price
