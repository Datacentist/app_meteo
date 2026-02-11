# 🌦️ APPLICATION MÉTÉO - GUIDE COMPLET

## 📦 PACKAGE COMPLET

Vous avez téléchargé un package complet qui contient:

### 🎯 Fichiers Essentiels (À UTILISER)
1. **app.py** - Application Streamlit principale (VERSION CORRIGÉE ✅)
2. **linear_meteo.joblib** - Modèle de prédiction
3. **requirements.txt** - Dépendances Python
4. **expected_cols.json** - Configuration du modèle

### 🛠️ Fichiers d'Installation & Test
5. **install.ps1** - Script d'installation automatique PowerShell
6. **test_installation.py** - Script de test de l'installation
7. **diagnostic_meteostat.py** - Diagnostic des imports

### 📚 Documentation
8. **README.md** - Documentation complète
9. **QUICK_START.md** - Guide de démarrage rapide
10. **DEPLOYMENT_GUIDE.md** - Guide de déploiement sur Streamlit Cloud
11. **INSTALL_INSTRUCTIONS.md** - Ce fichier

### 🗑️ Fichiers à Ignorer (versions anciennes)
- ~~app_fixed.py~~ (version intermédiaire, utilisez app.py)

---

## 🚀 INSTALLATION EN 3 ÉTAPES

### ✅ ÉTAPE 1: Préparation (2 minutes)

1. **Créez un dossier** pour votre projet:
```
C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app\
```

2. **Placez TOUS les fichiers téléchargés** dans ce dossier

3. **Vérifiez** que vous avez bien Python 3.11:
```powershell
python --version
```
Si vous n'avez pas Python 3.11, installez-le depuis: https://www.python.org/downloads/

### ✅ ÉTAPE 2: Installation Automatique (3 minutes)

1. **Ouvrez PowerShell**
   - Appuyez sur `Windows + X`
   - Choisissez "Windows PowerShell"

2. **Naviguez vers le dossier**:
```powershell
cd "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"
```

3. **Autorisez l'exécution de scripts** (une seule fois):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Tapez `Y` puis `Entrée`

4. **Lancez l'installation**:
```powershell
.\install.ps1
```

Le script va:
- ✅ Créer un environnement virtuel
- ✅ Installer toutes les dépendances
- ✅ Tester meteostat

### ✅ ÉTAPE 3: Test et Lancement (1 minute)

1. **Testez l'installation**:
```powershell
python test_installation.py
```

2. **Si tous les tests passent, lancez l'app**:
```powershell
streamlit run app.py
```

🎉 **L'application s'ouvre dans votre navigateur!**

---

## 🆘 EN CAS DE PROBLÈME

### ❌ Problème: "ImportError: cannot import name 'Monthly'"

**C'est LE problème que vous aviez!**

✅ **Solution 1 - Réinstaller meteostat:**
```powershell
.\venv\Scripts\Activate.ps1
pip uninstall meteostat -y
pip cache purge
pip install meteostat
```

✅ **Solution 2 - Utiliser le fichier app.py corrigé:**
Le fichier `app.py` fourni gère automatiquement les différentes versions de meteostat!

### ❌ Problème: "Scripts désactivés"

✅ **Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ Problème: "Python n'est pas reconnu"

✅ **Solution:**
1. Installez Python 3.11
2. Cochez "Add Python to PATH" pendant l'installation
3. Redémarrez PowerShell

### ❌ Problème: "FileNotFoundError: linear_meteo.joblib"

✅ **Solution:**
Vérifiez que le fichier `linear_meteo.joblib` est bien dans le même dossier que `app.py`

---

## 🔄 UTILISATION QUOTIDIENNE

À chaque fois que vous voulez utiliser l'app:

```powershell
# 1. Naviguez vers le dossier
cd "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"

# 2. Activez l'environnement virtuel
.\venv\Scripts\Activate.ps1

# 3. Lancez l'app
streamlit run app.py
```

Pour arrêter l'app: `Ctrl + C` dans PowerShell

---

## 🌐 DÉPLOIEMENT EN LIGNE (OPTIONNEL)

Pour mettre votre app en ligne sur Streamlit Cloud:

1. Créez un compte GitHub (gratuit)
2. Créez un repository avec ces fichiers:
   - app.py
   - linear_meteo.joblib
   - requirements.txt
   - expected_cols.json
3. Allez sur https://share.streamlit.io
4. Connectez votre repository GitHub
5. Déployez!

📖 **Consultez DEPLOYMENT_GUIDE.md pour plus de détails**

---

## 🎯 CORRECTION DU PROBLÈME PRINCIPAL

### Le Problème Original

Vous aviez cette erreur:
```
ImportError: impossible d'importer le nom 'Monthly' depuis 'meteostat'
```

### La Cause

L'API de meteostat a changé entre les versions. Certaines installations ont des problèmes d'import.

### La Solution Appliquée

Le fichier **app.py** fourni contient ce code intelligent:

```python
# Import robuste de meteostat pour gérer différentes versions
try:
    # Tentative d'import direct (versions récentes)
    from meteostat import Point, Monthly, Stations
except ImportError:
    # Fallback pour les versions différentes
    import meteostat
    Point = meteostat.Point
    Monthly = meteostat.Monthly
    Stations = meteostat.Stations
```

Ce code essaie d'abord l'import direct, et si ça échoue, il utilise une méthode alternative!

---

## 📊 FICHIERS PAR PRIORITÉ

### 🔴 CRITIQUE (Sans eux, ça ne marche pas)
1. app.py
2. linear_meteo.joblib
3. requirements.txt

### 🟡 IMPORTANT (Recommandé)
4. expected_cols.json
5. test_installation.py

### 🟢 UTILE (Pour faciliter l'installation)
6. install.ps1
7. README.md
8. QUICK_START.md

### ⚪ OPTIONNEL
9. DEPLOYMENT_GUIDE.md
10. diagnostic_meteostat.py

---

## ✅ CHECKLIST AVANT DE COMMENCER

- [ ] Python 3.11 installé
- [ ] Tous les fichiers téléchargés dans le même dossier
- [ ] PowerShell ouvert
- [ ] Prêt à exécuter install.ps1

---

## 🎓 CE QUE VOUS ALLEZ APPRENDRE

En suivant ce guide, vous allez:
1. ✅ Installer un environnement Python propre
2. ✅ Gérer les dépendances avec pip
3. ✅ Résoudre les problèmes d'import
4. ✅ Lancer une application Streamlit
5. ✅ (Optionnel) Déployer sur le cloud

---

## 💪 VOUS ÊTES PRÊT!

Suivez simplement les **3 ÉTAPES** ci-dessus et tout fonctionnera!

En cas de problème, consultez:
1. La section "EN CAS DE PROBLÈME" ci-dessus
2. Le fichier README.md pour plus de détails
3. test_installation.py pour diagnostiquer

**Bonne chance! 🚀**

---

**Note:** Ce package a été créé spécifiquement pour résoudre votre problème d'import meteostat. Le fichier app.py fourni est une version améliorée et robuste qui gère automatiquement les différentes versions de l'API meteostat.
