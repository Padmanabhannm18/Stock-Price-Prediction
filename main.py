import streamlit as st
import pandas as pd
from preprocessing import load_and_preprocess_data
from models import train_and_evaluate_models
from predict import predict_stock_price

# Streamlit app title
st.title("📈 Stock Price Prediction Application")
st.write("Upload your dataset and predict stock prices with various regression models.")

# File uploader
data_file = st.file_uploader("Upload CSV File", type=["csv"])

if data_file is not None:
    data = load_and_preprocess_data(data_file)

    if data:
        x_train_scaled = data["x_train_scaled"]
        x_test_scaled = data["x_test_scaled"]
        y_train = data["y_train"]
        y_test = data["y_test"]
        scaler = data["scaler"]
        ds = data["data"]

        st.success("✅ Dataset preprocessing completed!")

        # Training and evaluation
        status = st.empty()
        progress_bar = st.progress(0)

        best_model, best_model_name, best_r2, results = train_and_evaluate_models(
            x_train_scaled, y_train, x_test_scaled, y_test
        )
        progress_bar.progress(50)

        st.write(f"### 🏆 Best Model: {best_model_name}")
        st.write(f"🎯 R-squared Score: {best_r2:.4f}")

        # Display feature importance if applicable
        if hasattr(best_model, "feature_importances_"):
            feature_importance = best_model.feature_importances_
            st.write("### 🔍 Feature Importances:")
            feature_importance_df = pd.DataFrame({
                "Feature": ds.columns[1:-1],
                "Importance": feature_importance
            }).sort_values(by="Importance", ascending=False)
            st.dataframe(feature_importance_df)

        progress_bar.progress(75)

        # Prediction form
        with st.form("prediction_form"):
            st.subheader("📊 Make a Prediction")
            input_data = []
            for i, col in enumerate(ds.columns[1:-1]):
                value = st.number_input(f"{col}", value=0.0, key=f"input_{i}")
                input_data.append(value)

            submit_button = st.form_submit_button("Predict")

        if submit_button:
            prediction = predict_stock_price(best_model, scaler, input_data)
            st.write(f"### 📉 Predicted Stock Price: {prediction:.2f}")
            progress_bar.progress(100)
