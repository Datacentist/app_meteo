# 🌐 Déploiement sur Streamlit Cloud

Ce guide vous explique comment déployer votre application météo sur Streamlit Cloud pour qu'elle soit accessible en ligne.

## 📋 Prérequis

1. **Compte GitHub** (gratuit) - https://github.com
2. **Compte Streamlit Cloud** (gratuit) - https://share.streamlit.io

## 🚀 Étapes de Déploiement

### Étape 1: Créer un Repository GitHub

1. Connectez-vous sur https://github.com
2. Cliquez sur le bouton `+` en haut à droite > `New repository`
3. Nommez votre repository: `meteo-prediction-app`
4. Choisissez `Public`
5. Cliquez sur `Create repository`

### Étape 2: Uploader vos Fichiers

**Option A: Interface Web GitHub** (Plus Simple)
1. Dans votre repository, cliquez sur `Add file` > `Upload files`
2. Glissez-déposez ces fichiers:
   - `app.py`
   - `linear_meteo.joblib`
   - `requirements.txt`
   - `expected_cols.json`
   - `.gitignore`
   - `README.md`
3. Cliquez sur `Commit changes`

**Option B: Git en ligne de commande**
```bash
cd "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"

# Initialiser Git
git init

# Ajouter tous les fichiers
git add app.py linear_meteo.joblib requirements.txt expected_cols.json .gitignore README.md

# Commit
git commit -m "Initial commit - Application météo"

# Lier au repository GitHub (remplacez YOUR_USERNAME par votre nom d'utilisateur)
git remote add origin https://github.com/YOUR_USERNAME/meteo-prediction-app.git

# Pousser vers GitHub
git branch -M main
git push -u origin main
```

### Étape 3: Déployer sur Streamlit Cloud

1. Allez sur https://share.streamlit.io
2. Connectez-vous avec votre compte GitHub
3. Cliquez sur `New app`
4. Configurez:
   - **Repository:** Sélectionnez `meteo-prediction-app`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Cliquez sur `Deploy!`

⏳ Attendez 2-3 minutes pour le déploiement...

🎉 **Votre application est en ligne!**

Vous recevrez une URL comme: `https://your-app-name.streamlit.app`

## 📝 Fichiers Requis pour le Déploiement

Assurez-vous que ces fichiers sont bien sur GitHub:

```
meteo-prediction-app/
├── app.py                    ✅ (OBLIGATOIRE)
├── linear_meteo.joblib       ✅ (OBLIGATOIRE)
├── requirements.txt          ✅ (OBLIGATOIRE)
├── expected_cols.json        ✅ (OBLIGATOIRE)
├── .gitignore               ✅ (RECOMMANDÉ)
└── README.md                ✅ (RECOMMANDÉ)
```

❌ **NE PAS inclure:**
- Le dossier `venv/`
- Les fichiers `.bak`
- Les scripts de test (optionnel)

## 🔧 Configuration du requirements.txt

Votre `requirements.txt` doit contenir exactement:

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
joblib>=1.3.0
meteostat>=1.6.0
```

## 🐛 Dépannage

### Problème: "ModuleNotFoundError"
👉 Vérifiez que `requirements.txt` est bien présent et contient toutes les dépendances

### Problème: "FileNotFoundError: linear_meteo.joblib"
👉 Vérifiez que le fichier `.joblib` est bien uploadé sur GitHub

### Problème: L'application crash au démarrage
1. Regardez les logs dans Streamlit Cloud
2. Vérifiez que tous les fichiers sont présents
3. Testez localement d'abord avec `streamlit run app.py`

### Problème: "ImportError: cannot import name 'Monthly'"
👉 Mettez à jour `requirements.txt` avec `meteostat>=1.6.0`

## 🔄 Mettre à Jour l'Application

Pour mettre à jour votre application en ligne:

**Option A: GitHub Web**
1. Allez dans votre repository GitHub
2. Cliquez sur le fichier à modifier
3. Cliquez sur l'icône crayon ✏️
4. Faites vos modifications
5. Cliquez sur `Commit changes`

**Option B: Git**
```bash
# Modifiez vos fichiers localement
# Puis:
git add .
git commit -m "Description de vos changements"
git push
```

Streamlit Cloud redéploiera automatiquement! ♻️

## 🎨 Personnalisation

### Changer le nom de l'app
1. Allez sur Streamlit Cloud
2. Cliquez sur les 3 points ⋮ > `Settings`
3. Changez le nom sous `General`

### URL Personnalisée
L'URL sera basée sur votre nom d'app: `https://nom-app.streamlit.app`

## 💡 Astuces

- ✅ Testez toujours localement avant de déployer
- ✅ Utilisez des versions spécifiques dans `requirements.txt`
- ✅ Vérifiez les logs en cas d'erreur
- ✅ Gardez votre repository à jour

## 📊 Limites Gratuites de Streamlit Cloud

- **Ressources:** 1 GB RAM, CPU partagé
- **Nombre d'apps:** Illimité (public)
- **Uptime:** Pas de garantie (peut dormir après inactivité)

Pour plus de ressources, considérez Streamlit Cloud Pro.

## 🆘 Support

- Documentation Streamlit: https://docs.streamlit.io
- Forum Streamlit: https://discuss.streamlit.io
- GitHub Issues: Créez un issue dans votre repository

---

**Bonne chance avec votre déploiement! 🚀**
