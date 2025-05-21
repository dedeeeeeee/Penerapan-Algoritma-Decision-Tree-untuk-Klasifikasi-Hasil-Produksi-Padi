import streamlit as st
import pandas as pd

def app(x, model, le_prov, le_thn):
    st.title("Klasifikasi Hasil Produksi Padi ")

    provinsi = st.selectbox("Pilih Provinsi", le_prov.classes_)
    tahun = st.selectbox("Pilih Tahun", le_thn.classes_)

    if st.button("Klasifikasi"):
        prov_enc = le_prov.transform([provinsi])[0]
        thn_enc = le_thn.transform([tahun])[0]

        # Buat data prediksi
        X_pred = pd.DataFrame([[prov_enc, thn_enc]], columns=['Provinsi_enc', 'Tahun_enc'])

        hasil = model.predict(X_pred)[0]
        st.success(f"Hasil Panen provinsi **{provinsi}** pada tahun **{tahun}**: **{hasil}**")
