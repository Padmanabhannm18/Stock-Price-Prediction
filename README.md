# 📈 Real-Time Stock Price Prediction System

## 📌 Project Overview

This project is a **Real-Time Stock Price Prediction System** that leverages **machine learning models** to predict future stock prices based on historical data. The system fetches live stock data, processes it, trains various regression models, and provides predictions through an interactive **Streamlit** web application.

## 🎮 Project Structure

```
realtime_stock_prediction/
│── main.py                  # Main Streamlit UI
│── data_fetch.py             # Fetch real-time stock data
│── model_training.py         # Train and evaluate machine learning models
│── utils.py                  # Utility functions (data preprocessing, feature engineering)
│── requirements.txt          # Dependencies
│── README.md                 # Project Documentation
```

## 🔧 Installation and Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Padmanabhannm1/Stock-Price-Prediction.git
cd Stock-Price-Prediction
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

## 🚀 Running the Application

After installing dependencies, run the Streamlit app:

```sh
streamlit run main.py
```

## 📚 File Descriptions

### `main.py`

- **Streamlit UI** for real-time stock prediction.
- Allows users to **select a stock symbol**, choose a model, and predict future prices.

### `data_fetch.py`

- Fetches **real-time stock data** using `yfinance`.
- Prepares historical stock price data for model training.

### `model_training.py`

- Trains **multiple regression models** including:
  - Decision Tree Regressor
  - Random Forest Regressor
  - Support Vector Machine (SVR)
  - Bayesian Ridge Regression
  - Gradient Boosting
- Uses **GridSearchCV** for hyperparameter tuning.

### `utils.py`

- Handles **data preprocessing** (scaling, feature engineering, missing values).
- Provides helper functions for **model evaluation**.

## 💡 Features

✅ **Real-time stock data fetching** from Yahoo Finance.\
✅ **Multiple regression models** for price prediction.\
✅ **Hyperparameter tuning** for optimal performance.\
✅ **Interactive UI** with **Streamlit**.\
✅ **Feature importance analysis** for model interpretability.

## 📊 Example Output

### **User selects stock symbol: ****`AAPL`**** (Apple Inc.)**

- **Predicted Stock Price:** `$178.50`
- **Best Model:** `Random Forest Regressor`
- **R-squared Score:** `0.89`

## 💪 Contributing

Feel free to contribute by improving the models or adding new features!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## 📚 Technologies Used

- **Python** 🐍
- **Streamlit** 📊
- **Scikit-learn** 🤖
- **Yahoo Finance API (****`yfinance`****)** 📈
- **NumPy & Pandas** 📊

## 💎 License

This project is open-source and available under the **MIT License**.

---

🎬 **Happy Predicting!** ✨

