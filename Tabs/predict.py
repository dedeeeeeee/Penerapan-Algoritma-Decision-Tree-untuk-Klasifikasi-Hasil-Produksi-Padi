import streamlit as st
import numpy as np

def app(df, x, y, model):
    st.title("Prediksi Produksi Padi")

    st.write("Masukkan nilai untuk fitur-fitur berikut:")

    input_data = []
    for col in x.columns:
        val = st.number_input(f"{col}", value=float(df[col].mean()))
        input_data.append(val)

    if st.button("Prediksi"):
        prediction = model.predict([input_data])[0]
        label = {0: "Rendah", 1: "Sedang", 2: "Tinggi"}  # Pastikan urutan label sesuai
        st.success(f"Prediksi kategori produksi: **{label[prediction]}**")
