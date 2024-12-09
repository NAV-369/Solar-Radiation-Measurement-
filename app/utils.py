import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    # Simulate data loading
    data = {
        'Date': pd.date_range(start="2024-01-01", periods=365, freq="D"),
        'GHI': pd.Series(range(100, 1000)).sample(365, replace=True).reset_index(drop=True)
    }
    return pd.DataFrame(data)

def plot_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['GHI'], label="GHI", color='orange')
    plt.xlabel("Date")
    plt.ylabel("GHI")
    plt.title("GHI Over Time")
    plt.legend()
    st.pyplot(plt)