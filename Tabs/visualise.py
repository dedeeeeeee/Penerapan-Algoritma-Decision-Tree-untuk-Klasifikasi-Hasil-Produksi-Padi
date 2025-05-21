import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import plot_tree

def app(df, x, model):
    st.title("Visualisasi Data")

    # Histogram Produksi Padi
    st.subheader("📊 Histogram Produksi Padi")
    fig, ax = plt.subplots()
    df['Produksi'].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
    st.pyplot(fig)

    # Distribusi target_kategori
    st.subheader("📈 Distribusi Kategori Produksi")
    fig2, ax2 = plt.subplots()
    df['target_kategori'].value_counts().plot(kind='bar', ax=ax2, color='orange')
    ax2.set_xlabel("Kategori")
    ax2.set_ylabel("Jumlah")
    st.pyplot(fig2)

    # Heatmap Korelasi
    st.subheader("🔥 Korelasi Antar Fitur")
    fig4, ax4 = plt.subplots()
    corr = df[['Produksi', 'Provinsi_enc', 'Tahun_enc']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax4)
    st.pyplot(fig4)

    # Confusion Matrix
    st.subheader("📉 Confusion Matrix")
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # Buat ulang model untuk evaluasi (jika belum split)
    X = df[['Provinsi_enc', 'Tahun_enc']]
    y = df['target_kategori']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=["Rendah", "Sedang", "Tinggi"])

    fig_cm, ax_cm = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Rendah", "Sedang", "Tinggi"])
    disp.plot(ax=ax_cm, cmap='Blues')
    st.pyplot(fig_cm)

    # Diagram Decision Tree
    st.subheader("🌳 Diagram Pohon Keputusan (Decision Tree)")
    fig3, ax3 = plt.subplots(figsize=(16, 8))
    plot_tree(model,
              feature_names=X.columns,
              class_names=["Rendah", "Sedang", "Tinggi"],
              filled=True, rounded=True, fontsize=10, ax=ax3)
    st.pyplot(fig3)
