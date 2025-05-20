import streamlit as st
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

def app(df, x, y, model):
    st.title("Visualisasi Data")

    # Histogram Produksi
    st.subheader("Histogram Produksi Padi")
    fig, ax = plt.subplots()
    df['Produksi'].hist(ax=ax, bins=20)
    st.pyplot(fig)

    # Distribusi Kategori
    st.subheader("Distribusi Kategori Produksi")
    fig2, ax2 = plt.subplots()
    df['target_kategori'].value_counts().plot(kind='bar', ax=ax2)
    st.pyplot(fig2)

    # Diagram Pohon Keputusan
    st.subheader("Diagram Pohon Keputusan (Decision Tree)")
    fig3, ax3 = plt.subplots(figsize=(16, 8))
    plot_tree(model, feature_names=x.columns, class_names=["Rendah", "Sedang", "Tinggi"],
              filled=True, rounded=True, fontsize=10, ax=ax3)
    st.pyplot(fig3)
