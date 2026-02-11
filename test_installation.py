"""
Script de test pour l'application météo
Compatible Meteostat 1.6.5
"""

import sys
import os
from datetime import datetime, timedelta
import joblib

print("╔" + "=" * 58 + "╗")
print("║" + " " * 16 + "TEST DE L'APPLICATION MÉTÉO" + " " * 15 + "║")
print("╚" + "=" * 58 + "╝")

# ==========================
# Test des imports
# ==========================
print("=" * 60)
print("TEST DES IMPORTS")
print("=" * 60)

imports_status = {}

# Librairies de base
for lib, name in [(("streamlit",), "streamlit"),
                  (("pandas",), "pandas"),
                  (("numpy",), "numpy"),
                  (("sklearn",), "scikit-learn"),
                  (("joblib",), "joblib")]:
    try:
        module = __import__(lib[0])
        version = getattr(module, "__version__", "inconnu")
        print(f"✓ {name} {version}")
        imports_status[name] = True
    except ImportError as e:
        print(f"✗ {name}: {e}")
        imports_status[name] = False

# Meteostat 1.6.5 compatible
try:
    import meteostat
    print(f"✓ meteostat {meteostat.__version__} importé correctement")
    imports_status['meteostat'] = True
except ImportError as e:
    print(f"✗ meteostat: {e}")
    imports_status['meteostat'] = False

# ==========================
# Résumé imports
# ==========================
print("=" * 60)
if all(imports_status.values()):
    print("✓ TOUS LES IMPORTS ONT RÉUSSI!")
else:
    print("✗ CERTAINS IMPORTS ONT ÉCHOUÉ:")
    for module, status in imports_status.items():
        if not status:
            print(f"  - {module}")
print("=" * 60)

# ==========================
# Test du fichier modèle
# ==========================
print("=" * 60)
print("TEST DU FICHIER MODÈLE")
print("=" * 60)

model_path = "linear_meteo.joblib"
model_loaded = False

if os.path.exists(model_path):
    print(f"✓ Fichier '{model_path}' trouvé!")
    try:
        model = joblib.load(model_path)
        print(f"✓ Modèle chargé avec succès! ({type(model).__name__})")
        model_loaded = True
    except Exception as e:
        print(f"✗ Erreur lors du chargement du modèle: {e}")
else:
    print(f"✗ Fichier '{model_path}' non trouvé!")

# ==========================
# Test de connexion Meteostat
# ==========================
print("=" * 60)
print("TEST DE CONNEXION METEOSTAT")
print("=" * 60)

meteostat_connected = False

if imports_status.get('meteostat', False):
    try:
        lat, lon = 14.7167, -17.4677
        start = datetime.today() - timedelta(days=365)
        end = datetime.today()

        # Recherche d'une station proche
        stations = meteostat.Stations().nearby(lat, lon).fetch(1)
        if not stations.empty:
            station_id = stations.index[0]
            station_name = stations.iloc[0]['name']
            print(f"✓ Station trouvée: {station_name} ({station_id})")

            # Récupération des données mensuelles
            data = meteostat.Monthly(station_id, start, end).fetch()
            if not data.empty:
                print("✓ Données météo récupérées avec succès !")
                meteostat_connected = True
            else:
                print("⚠ Connexion OK mais aucune donnée récupérée")
        else:
            print("⚠ Aucune station trouvée")

    except Exception as e:
        print(f"✗ Erreur Meteostat: {e}")
else:
    print("⚠ Meteostat non importé correctement")

# ==========================
# Résumé final
# ==========================
print("=" * 60)
print("RÉSUMÉ DES TESTS")
print("=" * 60)
print(f"Imports de base: {'✓ RÉUSSI' if all(imports_status.values()) else '✗ ÉCHOUÉ'}")
print(f"Fichier modèle: {'✓ RÉUSSI' if model_loaded else '✗ ÉCHOUÉ'}")
print(f"Connexion Meteostat: {'✓ RÉUSSI' if meteostat_connected else '✗ ÉCHOUÉ'}")
print("=" * 60)

if all(imports_status.values()) and model_loaded and meteostat_connected:
    print("✓ TOUS LES TESTS ONT RÉUSSI!")
    print("  Vous pouvez lancer l'application avec: streamlit run app.py")
else:
    print("✗ CERTAINS TESTS ONT ÉCHOUÉ")
    print("  Corrigez les erreurs ci-dessus avant de lancer l'application")
