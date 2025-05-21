import streamlit as st
from Tabs import home, predict, visualise

import pandas as pd
from web_functions import load_model

# Load data dan model
df = pd.read_csv("Padi.csv")
x, model, le_prov, le_thn = load_model(df)

# Sidebar Navigasi
page = st.sidebar.selectbox("Navigasi", ("Beranda", "Prediksi", "Visualisasi"))

if page == "Beranda":
    home.app()
elif page == "Prediksi":
    predict.app(x, model, le_prov, le_thn)
elif page == "Visualisasi":
    visualise.app(df, x, model)
