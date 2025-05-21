import streamlit as st

def app():
    st.markdown("<h1 style='text-align: center;'>🌾 Aplikasi Klasifikasi Produksi Padi </h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: justify; font-size: 16px;'>
    Selamat datang di <strong>Aplikasi Klasifikasi Produksi Padi</strong>!<br><br>

    Aplikasi ini menggunakan algoritma <strong style='color:#1f77b4;'>Decision Tree</strong> untuk mengklasifikasi kategori hasil panen padi di Indonesia berdasarkan <strong>Provinsi</strong> dan <strong>Tahun</strong> tertentu.<br>

    Kategori Klasifikasi dibagi menjadi: 
    <ul>
        <li><strong style='color:green;'>Tinggi</strong> - Produksi sangat tinggi</li>
        <li><strong style='color:orange;'>Sedang</strong> - Produksi sedang</li>
        <li><strong style='color:red;'>Rendah</strong> - Produksi rendah</li>
    </ul>

    🎯 <strong>Tujuan aplikasi:</strong>  
    Membantu analisis dan pengambilan keputusan dalam sektor pertanian, khususnya dalam mengidentifikasi pola hasil panen di berbagai daerah dan tahun.<br>
    🔍 <strong>Sumber Data:</strong>  
    Dataset ini berisi informasi mengenai hasil produksi padi tahunan dari berbagai provinsi di Pulau Sumatera, Indonesia. Data mencakup periode tahun 1993 hingga 2020 dan terdiri dari variabel-variabel agrikultur serta iklim.
    
    Klik menu di sebelah kiri untuk mulai melakukan <strong>klasifikasi</strong> atau <strong>visualisasi data</strong> 📊.
    </div>
    """, unsafe_allow_html=True)
