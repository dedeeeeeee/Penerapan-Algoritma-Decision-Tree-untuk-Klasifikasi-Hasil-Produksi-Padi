import streamlit as st
from web_functions import load_data
from Tabs import home, predict, visualise

Tabs = {
    "Home": home.app,
    "Prediction": predict.app,
    "Visualisation": visualise.app
}

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", list(Tabs.keys()))

df, x, y, model = load_data()

if page in ["Prediction", "Visualisation"]:
    Tabs[page](df, x, y, model)
else:
    Tabs[page]()
