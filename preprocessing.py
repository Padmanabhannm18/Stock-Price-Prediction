import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

@st.cache_data
def load_and_preprocess_data(data_file):
    """Loads and preprocesses the dataset."""
    try:
        ds = pd.read_csv(data_file)
        st.subheader("Dataset Overview")
        st.dataframe(ds.head())

        if ds.shape[1] < 2:
            st.error("Dataset must have at least two columns: features and target.")
            return None

        x = ds.iloc[:, 1:-1].values  # Features
        y = ds.iloc[:, -1].values   # Target

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        x_train_scaled = scaler.fit_transform(x_train)
        x_test_scaled = scaler.transform(x_test)

        return {
            "data": ds,
            "x_train_scaled": x_train_scaled,
            "x_test_scaled": x_test_scaled,
            "y_train": y_train,
            "y_test": y_test,
            "scaler": scaler
        }
    except Exception as e:
        st.error(f"Error processing the dataset: {e}")
        return None
