# 📈 Stock Price Prediction Application

This project is a **Stock Price Prediction Application** built with **Streamlit**. It allows users to upload a dataset and apply various regression models to predict stock prices. The application automatically preprocesses the data, trains multiple machine learning models, and selects the best-performing model based on the R-squared score.

---

## 🚀 Features
- 📂 **Upload CSV Dataset** – Accepts user-provided data for training models.
- 📊 **Automated Data Preprocessing** – Scales features using StandardScaler.
- 🏆 **Multiple Regression Models** – Supports Decision Tree, Random Forest, K-Nearest Neighbors, Support Vector Machine, Bayesian Ridge, and Gradient Boosting.
- 🔎 **Hyperparameter Tuning** – Uses GridSearchCV to optimize model parameters.
- 📈 **Best Model Selection** – Chooses the model with the highest R-squared score.
- 🔍 **Feature Importance Analysis** – Displays feature importance for tree-based models.
- 📉 **Stock Price Prediction** – Allows users to input new data for prediction.

---

## 📂 Project Structure
```
stock_price_prediction/
│── main.py                 # Streamlit UI
│── preprocessing.py         # Data loading & preprocessing
│── models.py                # Model training & evaluation
│── predict.py               # Prediction logic
│── data/                    # Folder for datasets
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

---

## 🛠 Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Padmanabhannm18/stock-price-prediction.git
cd stock-price-prediction
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application
```bash
streamlit run main.py
```

---

## 📌 Usage
1️⃣ Upload a CSV file with historical stock price data.
2️⃣ The app preprocesses and splits the data into training and testing sets.
3️⃣ Multiple regression models are trained, and the best one is selected.
4️⃣ View model performance and feature importance.
5️⃣ Input custom values to predict stock prices.

---

## 📊 Supported Models
- Decision Tree Regressor 🌳
- Random Forest Regressor 🌲
- K-Nearest Neighbors 🤝
- Support Vector Regressor 🏹
- Bayesian Ridge 🔵
- Gradient Boosting 🔥

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ✨ Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 💡 Future Enhancements
- ✅ Add LSTM and deep learning models for time series forecasting.
- ✅ Implement real-time stock data fetching using APIs.
- ✅ Enhance UI with interactive visualizations.

---

## 📩 Contact
For any questions or issues, reach out via **your-email@example.com** or create an issue in the GitHub repository.

---

🚀 **Happy Coding!**

