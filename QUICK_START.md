# 🚀 DÉMARRAGE RAPIDE

## Installation Express (5 minutes)

### 1️⃣ Préparez les fichiers
Téléchargez tous les fichiers et placez-les dans un dossier, par exemple:
```
C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app\
```

### 2️⃣ Ouvrez PowerShell
- Appuyez sur `Windows + X`
- Sélectionnez "Windows PowerShell"

### 3️⃣ Naviguez vers le dossier
```powershell
cd "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"
```

### 4️⃣ Autorisez l'exécution de scripts (une seule fois)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Tapez `Y` puis `Entrée`

### 5️⃣ Lancez l'installation automatique
```powershell
.\install.ps1
```
⏳ Attendez 2-3 minutes...

### 6️⃣ Testez l'installation
```powershell
python test_installation.py
```
✅ Vérifiez que tous les tests passent

### 7️⃣ Lancez l'application
```powershell
streamlit run app.py
```
🎉 L'application s'ouvre dans votre navigateur!

---

## ⚡ Commandes Essentielles

**Activer l'environnement virtuel** (à faire à chaque fois):
```powershell
.\venv\Scripts\Activate.ps1
```

**Lancer l'application**:
```powershell
streamlit run app.py
```

**Arrêter l'application**:
Appuyez sur `Ctrl + C` dans PowerShell

---

## 🆘 En cas de problème

### Problème #1: "Python n'est pas reconnu..."
👉 Installez Python 3.11 depuis: https://www.python.org/downloads/
✓ Cochez "Add Python to PATH" pendant l'installation

### Problème #2: "Impossible d'importer meteostat"
```powershell
.\venv\Scripts\Activate.ps1
pip uninstall meteostat -y
pip install meteostat
```

### Problème #3: "Scripts désactivés"
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problème #4: L'application ne se lance pas
1. Vérifiez que tous les fichiers sont présents
2. Exécutez: `python test_installation.py`
3. Vérifiez les messages d'erreur

---

## 📂 Fichiers Requis

Vérifiez que vous avez ces 7 fichiers:

- ✅ `app.py` (Application principale)
- ✅ `linear_meteo.joblib` (Modèle)
- ✅ `requirements.txt` (Dépendances)
- ✅ `expected_cols.json` (Configuration)
- ✅ `test_installation.py` (Tests)
- ✅ `install.ps1` (Installation)
- ✅ `README.md` (Documentation)

---

## 🎯 Utilisation

1. **Entrez les coordonnées** (Dakar par défaut)
2. **Cliquez sur "Prédire"**
3. **Consultez la prévision**

**C'est aussi simple que ça!** 🎉
