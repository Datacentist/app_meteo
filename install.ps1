# ========================================
# GUIDE D'INSTALLATION - Application Météo
# ========================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "INSTALLATION DE L'APPLICATION METEO" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Étape 1: Vérifier Python
Write-Host "[1/6] Vérification de Python 3.11..." -ForegroundColor Yellow
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR: Python n'est pas installé ou n'est pas dans le PATH!" -ForegroundColor Red
    Write-Host "Installez Python 3.11 depuis https://www.python.org/downloads/" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Python trouvé!`n" -ForegroundColor Green

# Étape 2: Naviguer vers le dossier
Write-Host "[2/6] Navigation vers le dossier du projet..." -ForegroundColor Yellow
$projectPath = "C:\Users\7MAKSACOD PC\meteo-prediction-app\meteo_app"
if (Test-Path $projectPath) {
    Set-Location $projectPath
    Write-Host "✓ Dossier trouvé: $projectPath`n" -ForegroundColor Green
} else {
    Write-Host "Création du dossier: $projectPath" -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $projectPath -Force | Out-Null
    Set-Location $projectPath
    Write-Host "✓ Dossier créé!`n" -ForegroundColor Green
}

# Étape 3: Supprimer l'ancien environnement virtuel si existant
Write-Host "[3/6] Nettoyage de l'ancien environnement virtuel..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Remove-Item -Recurse -Force venv
    Write-Host "✓ Ancien environnement supprimé!`n" -ForegroundColor Green
} else {
    Write-Host "✓ Pas d'ancien environnement à supprimer.`n" -ForegroundColor Green
}

# Étape 4: Créer un nouvel environnement virtuel
Write-Host "[4/6] Création d'un nouvel environnement virtuel..." -ForegroundColor Yellow
python -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR: Impossible de créer l'environnement virtuel!" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Environnement virtuel créé!`n" -ForegroundColor Green

# Étape 5: Activer l'environnement virtuel
Write-Host "[5/6] Activation de l'environnement virtuel..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR lors de l'activation. Essayez manuellement:" -ForegroundColor Red
    Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    Write-Host "Puis réexécutez ce script." -ForegroundColor Yellow
    exit 1
}
Write-Host "✓ Environnement activé!`n" -ForegroundColor Green

# Étape 6: Installer les dépendances
Write-Host "[6/6] Installation des dépendances..." -ForegroundColor Yellow
Write-Host "Cela peut prendre quelques minutes...`n" -ForegroundColor Yellow

python -m pip install --upgrade pip
pip install streamlit pandas numpy scikit-learn joblib meteostat

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR lors de l'installation des dépendances!" -ForegroundColor Red
    exit 1
}

Write-Host "`n✓ Toutes les dépendances installées!`n" -ForegroundColor Green

# Vérification finale
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "VÉRIFICATION DE L'INSTALLATION" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Test d'import de meteostat..." -ForegroundColor Yellow
python -c "from meteostat import Point, Monthly, Stations; print('✓ Tous les imports réussis!')"

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "✓ INSTALLATION TERMINÉE AVEC SUCCÈS!" -ForegroundColor Green
    Write-Host "========================================`n" -ForegroundColor Green
    
    Write-Host "PROCHAINES ÉTAPES:" -ForegroundColor Cyan
    Write-Host "1. Placez les fichiers suivants dans ce dossier:" -ForegroundColor White
    Write-Host "   - app.py" -ForegroundColor Yellow
    Write-Host "   - linear_meteo.joblib" -ForegroundColor Yellow
    Write-Host "   - requirements.txt" -ForegroundColor Yellow
    Write-Host "`n2. Lancez l'application:" -ForegroundColor White
    Write-Host "   streamlit run app.py`n" -ForegroundColor Yellow
} else {
    Write-Host "`nERREUR: L'import de meteostat a échoué!" -ForegroundColor Red
    Write-Host "Essayez de réinstaller meteostat manuellement:" -ForegroundColor Yellow
    Write-Host "pip uninstall meteostat -y" -ForegroundColor White
    Write-Host "pip install meteostat`n" -ForegroundColor White
}
