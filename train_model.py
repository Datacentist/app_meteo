import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Exemple minimal de données (à remplacer par tes vraies données historiques)
data = {
    "month": [1, 2, 3, 4, 5],
    "year": [2020, 2020, 2020, 2020, 2020],
    "tavg_lag1": [20.0, 21.0, 22.0, 21.5, 22.5],
    "tavg": [21.0, 22.0, 22.5, 22.0, 23.0]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Sélection des features et de la target
X = df[["month", "year", "tavg_lag1"]]
y = df["tavg"]

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X, y)

# Sauvegarde du modèle dans le fichier linear_meteo.joblib
joblib.dump(model, "linear_meteo.joblib")

print("✅ Modèle entraîné et sauvegardé avec succès !")
