import streamlit as st

def app():
    st.title("Aplikasi Prediksi Produksi Padi")
    st.write("""
        Selamat datang di aplikasi prediksi klasifikasi produksi padi menggunakan algoritma Decision Tree.
        Aplikasi ini memiliki 3 menu:
        - **Home**: Halaman ini.
        - **Prediction**: Masukkan fitur untuk memprediksi hasil produksi (Rendah/Sedang/Tinggi).
        - **Visualisation**: Lihat ringkasan dan grafik data.
    """)
