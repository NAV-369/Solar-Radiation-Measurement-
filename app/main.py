import streamlit as st
from app.utils import load_data, plot_chart

# App Title
st.title("Solar Radiation Dashboard")

# Sidebar: Filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Select Date Range")
ghi_threshold = st.sidebar.slider("GHI Threshold", 0, 1000, 500)

# Load Data
data = load_data()

# Filter Data
filtered_data = data[data['GHI'] > ghi_threshold]

# Main Dashboard Section
st.header("Filtered Data Insights")
st.dataframe(filtered_data)

# Plot Chart
st.header("Solar Radiation Over Time")
plot_chart(filtered_data)