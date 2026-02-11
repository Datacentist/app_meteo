# 🌦️ Application de Prévision Météo Mensuelle

Application Streamlit utilisant un modèle de régression linéaire pour prédire la température moyenne du mois suivant basée sur les données Meteostat.

## 📋 Prérequis

- **Python 3.11** (obligatoire pour Streamlit)
- **Windows PowerShell** (pour l'installation)

## 🚀 Installation Automatique

### Méthode 1: Script PowerShell (RECOMMANDÉ)

1. Ouvrez PowerShell en tant qu'administrateur
2. Naviguez vers le dossier où se trouve `install.ps1`
3. Si c'est votre première fois, autorisez l'exécution de scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
4. Exécutez le script d'installation:
```powershell
.\install.ps1
```

Le script va automatiquement:
- ✅ Vérifier Python 3.11
- ✅ Créer un environnement virtuel propre
- ✅ Installer toutes les dépendances
- ✅ Tester l'installation

## 📦 Installation Manuelle

Si le script automatique ne fonctionne pas, suivez ces étapes:

### Étape 1: Créer l'environnement virtuel
```powershell
cd "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"
python -m venv venv
```

### Étape 2: Activer l'environnement
```powershell
.\venv\Scripts\Activate.ps1
```

### Étape 3: Mettre à jour pip
```powershell
python -m pip install --upgrade pip
```

### Étape 4: Installer les dépendances
```powershell
pip install streamlit pandas numpy scikit-learn joblib meteostat
```

## 📁 Structure des Fichiers

Assurez-vous d'avoir ces fichiers dans le même dossier:

```
meteo_app/
├── app.py                    # Application Streamlit principale
├── linear_meteo.joblib       # Modèle pré-entraîné
├── requirements.txt          # Liste des dépendances
├── test_installation.py      # Script de test
├── install.ps1              # Script d'installation (optionnel)
└── venv/                    # Environnement virtuel (créé automatiquement)
```

## 🧪 Tester l'Installation

Avant de lancer l'application, testez que tout fonctionne:

```powershell
python test_installation.py
```

Ce script va vérifier:
- ✅ Tous les imports Python
- ✅ Le fichier du modèle
- ✅ La connexion à Meteostat

## ▶️ Lancer l'Application

Une fois l'installation terminée et testée:

```powershell
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse: `http://localhost:8501`

## 🎯 Utilisation

1. **Entrez les coordonnées** (latitude/longitude) de votre localisation
   - Exemple pour Dakar: Lat: 14.7167, Lon: -17.4677

2. **Ajustez les paramètres** (optionnel)
   - Minimum de mois requis: contrôle la qualité des données

3. **Cliquez sur "Prédire le mois suivant"**

4. **Consultez les résultats**:
   - Prédiction de température
   - Graphique de l'historique
   - Statistiques détaillées

## 🔧 Dépannage

### Problème: `ImportError: cannot import name 'Monthly' from 'meteostat'`

**Solution:**
```powershell
pip uninstall meteostat -y
pip install meteostat --upgrade
```

### Problème: `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problème: `FileNotFoundError: linear_meteo.joblib`

**Solution:** Assurez-vous que le fichier `linear_meteo.joblib` est dans le même dossier que `app.py`

### Problème: Aucune donnée récupérée pour ma localisation

**Solutions:**
- Vérifiez que les coordonnées sont correctes
- Essayez une localisation proche d'une grande ville
- Réduisez le slider "Minimum de mois requis"

## 📊 Données et Modèle

- **Source des données:** [Meteostat](https://meteostat.net/)
- **Modèle:** LinearRegression (scikit-learn)
- **Features utilisées:**
  - Mois de l'année
  - Année
  - Température du mois précédent (tavg_lag1)

## 🌍 Exemples de Coordonnées

| Ville | Latitude | Longitude |
|-------|----------|-----------|
| Dakar, Sénégal | 14.7167 | -17.4677 |
| Paris, France | 48.8566 | 2.3522 |
| New York, USA | 40.7128 | -74.0060 |
| Tokyo, Japon | 35.6762 | 139.6503 |

## 📝 Notes Importantes

1. **Python 3.11 requis** - Streamlit ne fonctionne pas avec toutes les versions
2. **Connexion Internet** - Nécessaire pour récupérer les données Meteostat
3. **Première exécution** - Peut être plus lente (téléchargement de données)
4. **Qualité des données** - Varie selon la localisation

## 🆘 Support

Si vous rencontrez des problèmes:

1. Exécutez `python test_installation.py` pour diagnostiquer
2. Vérifiez que vous utilisez Python 3.11
3. Assurez-vous que tous les fichiers sont présents
4. Relancez le script d'installation

## 📄 Licence

Ce projet utilise:
- Meteostat (données météorologiques)
- Streamlit (interface web)
- scikit-learn (modèle ML)

---

**Créé avec ❤️ pour la prévision météorologique**
