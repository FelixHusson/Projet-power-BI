import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

# Résoudre les chemins
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "clients_engineered_R.csv"

print("Chargement :", DATA_PATH)

df = pd.read_csv(DATA_PATH)

# Convertir les catégories en variables numériques
df = pd.get_dummies(df, drop_first=True)

# Vérifier la présence de churn
if "churn" not in df.columns:
    raise ValueError("La colonne 'churn' est introuvable dans le CSV !")

# 2. Séparer features / target
X = df.drop("churn", axis=1)
y = df["churn"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
import json
import os

columns_path = os.path.join("../models", "columns.json")

with open(columns_path, "w") as f:
    json.dump(list(X_train.columns), f)

# 4. Modèle
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# 5. Évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 6. Sauvegarde du modèle
MODEL_PATH = BASE_DIR / "models" / "model.pkl"
joblib.dump(model, MODEL_PATH)

print("✅ Modèle sauvegardé dans :", MODEL_PATH)
