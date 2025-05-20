import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def load_data():
    data = pd.read_csv("Padi.csv")

    # Encoding
    data_encoded = data.copy()
    label_encoders = {}

    for col in data_encoded.select_dtypes(include=['object']).columns:
        if col != 'Produksi':
            le = LabelEncoder()
            data_encoded[col] = le.fit_transform(data_encoded[col])
            label_encoders[col] = le

    # Binning target
    data_encoded['target_kategori'] = pd.cut(
        data_encoded['Produksi'],
        bins=3,
        labels=['Rendah', 'Sedang', 'Tinggi']
    )

    # Encode target
    le_target = LabelEncoder()
    y = le_target.fit_transform(data_encoded['target_kategori'])

    X = data_encoded.drop(columns=['Produksi', 'target_kategori'])

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X, y)

    return data_encoded, X, y, model
