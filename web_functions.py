import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def load_model(df):
    # Ubah Produksi jadi kategori
    def kategori(ton):
        if ton < 100000:
            return "Rendah"
        elif ton < 500000:
            return "Sedang"
        else:
            return "Tinggi"

    df['target_kategori'] = df['Produksi'].apply(kategori)

    # Label encoding
    le_prov = LabelEncoder()
    le_thn = LabelEncoder()

    df['Provinsi_enc'] = le_prov.fit_transform(df['Provinsi'])
    df['Tahun_enc'] = le_thn.fit_transform(df['Tahun'])

    x = df[['Provinsi', 'Tahun', 'Produksi', 'target_kategori']].copy()

    X_model = df[['Provinsi_enc', 'Tahun_enc']]
    y_model = df['target_kategori']

    clf = DecisionTreeClassifier()
    clf.fit(X_model, y_model)

    return x, clf, le_prov, le_thn
