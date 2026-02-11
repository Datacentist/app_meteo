import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, timedelta

# Configuration de la page Streamlit
st.set_page_config(page_title="Prévision mensuelle Meteostat", layout="centered")
st.title("Prévision météo mensuelle - LinearRegression")

# Import robuste de meteostat pour gérer différentes versions
try:
    # Tentative d'import direct (versions récentes)
    from meteostat import Point, Monthly, Stations
    METEOSTAT_IMPORT_METHOD = "direct"
except ImportError:
    # Fallback pour les versions plus anciennes ou différentes structures
    try:
        import meteostat
        Point = meteostat.Point
        Monthly = meteostat.Monthly
        Stations = meteostat.Stations
        METEOSTAT_IMPORT_METHOD = "module"
    except (ImportError, AttributeError) as e:
        st.error(f"""
        ❌ Erreur lors de l'import de meteostat: {str(e)}
        
        Veuillez installer meteostat correctement:
        ```
        pip install meteostat>=1.6.0
        ```
        """)
        st.stop()

# Fonction pour charger le modèle (mise en cache pour éviter de recharger à chaque interaction)
@st.cache_resource
def load_model():
    """Charge le modèle de régression linéaire pré-entraîné"""
    try:
        return joblib.load("linear_meteo.joblib")
    except FileNotFoundError:
        st.error("""
        ❌ Fichier 'linear_meteo.joblib' introuvable!
        
        Assurez-vous que le fichier est dans le même dossier que app.py
        """)
        st.stop()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle: {str(e)}")
        st.stop()

# Charger le modèle
model = load_model()

# Interface utilisateur - Localisation
st.subheader("📍 Localisation")
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", value=14.7167, format="%.6f", 
                         help="Latitude de la localisation (ex: 14.7167 pour Dakar)")
with col2:
    lon = st.number_input("Longitude", value=-17.4677, format="%.6f",
                         help="Longitude de la localisation (ex: -17.4677 pour Dakar)")

# Paramètres de qualité des données
st.subheader("⚙️ Paramètres")
min_months = st.slider(
    "Minimum de mois requis (qualité des données)", 
    min_value=6, 
    max_value=60, 
    value=18,
    help="Nombre minimum de mois de données valides requis pour faire une prédiction"
)

# Option de débogage
debug = st.checkbox("🔍 Afficher les informations de débogage", value=False)

def get_monthly_from_best_source(lat, lon, start, end):
    """
    Récupère des données mensuelles Meteostat avec stratégie de fallback
    
    Stratégie:
    1. Essayer les données directes par point (lat/lon)
    2. Si insuffisant, chercher une station météo proche
    
    Returns:
        tuple: (DataFrame, source_text) - les données et la source utilisée
    """
    try:
        # 1) Tentative avec Point direct
        p = Point(lat, lon)
        
        try:
            df_point = Monthly(p, start, end).fetch()
        except Exception as e:
            st.warning(f"Avertissement lors de la récupération des données par point: {str(e)}")
            df_point = pd.DataFrame()
        
        source = "Point(lat/lon)"
        
        # Vérifier si assez de données valides
        if not df_point.empty:
            non_na = 0
            if "tavg" in df_point.columns:
                non_na = df_point["tavg"].notna().sum()
            elif "tmin" in df_point.columns and "tmax" in df_point.columns:
                non_na = ((df_point["tmin"].notna()) & (df_point["tmax"].notna())).sum()
            
            if non_na >= min_months:
                return df_point, source
        
        # 2) Fallback: chercher une station proche
        try:
            # Essayer différentes syntaxes selon la version de meteostat
            try:
                # Nouvelle API
                stations = Stations().nearby(lat, lon).fetch(5)
            except TypeError:
                # Ancienne API
                stations = Stations().nearby(lat, lon, 5).fetch()
            
            if stations.empty:
                return pd.DataFrame(), "Aucune station proche trouvée"
            
            # Prendre la première station (la plus proche)
            station_id = stations.index[0]
            station_name = stations.iloc[0]['name'] if 'name' in stations.columns else station_id
            
            df_station = Monthly(station_id, start, end).fetch()
            return df_station, f"Station proche: {station_name} ({station_id})"
            
        except Exception as e:
            return pd.DataFrame(), f"Erreur lors de la recherche de stations: {str(e)}"
            
    except Exception as e:
        return pd.DataFrame(), f"Erreur générale: {str(e)}"

# Bouton de prédiction
if st.button("🔮 Prédire le mois suivant (tavg)", type="primary"):
    with st.spinner("Récupération des données météorologiques..."):
        # Définir la période de données
        end = datetime.today()
        start = end - timedelta(days=365 * 15)  # 15 ans pour maximiser l'historique
        
        # Récupérer les données
        df, source_used = get_monthly_from_best_source(lat, lon, start, end)
        
        if df.empty:
            st.error("""
            ❌ Aucune donnée Meteostat exploitable pour cette localisation.
            
            Suggestions:
            - Vérifiez les coordonnées (latitude/longitude)
            - Essayez une localisation proche d'une grande ville
            - Réduisez le nombre minimum de mois requis
            """)
            st.stop()
        
        # Affichage des informations de débogage
        if debug:
            st.info(f"**Source utilisée:** {source_used}")
            st.write(f"**Méthode d'import meteostat:** {METEOSTAT_IMPORT_METHOD}")
            st.write(f"**Colonnes disponibles:** {list(df.columns)}")
            
            # Comptage des valeurs non-nulles
            counts = {col: int(df[col].notna().sum()) for col in df.columns}
            st.write("**Nombre de valeurs non-NaN par colonne:**")
            st.json(counts)
            
            st.write("**Aperçu des dernières données:**")
            st.dataframe(df.tail(12))
        
        # Traitement de tavg (température moyenne)
        if ("tavg" not in df.columns) or df["tavg"].isna().all():
            if ("tmin" in df.columns) and ("tmax" in df.columns):
                st.warning("⚠️ tavg indisponible → calculé via (tmin + tmax) / 2")
                df["tavg"] = (df["tmin"] + df["tmax"]) / 2
            else:
                st.error("""
                ❌ Température moyenne (tavg) indisponible et impossible à reconstruire.
                
                Aucune donnée tmin/tmax disponible pour cette localisation.
                """)
                st.stop()
        
        # Garder seulement les lignes où tavg existe
        df = df.dropna(subset=["tavg"])
        
        # Vérifier la quantité minimale de données
        if df.shape[0] < max(2, min_months):
            st.error(f"""
            ❌ Données insuffisantes: seulement {df.shape[0]} mois valides 
            (minimum requis: {min_months})
            
            Essayez:
            - Une autre localisation
            - Réduire le slider "Minimum de mois requis"
            """)
            st.stop()
        
        # Transformation de l'index en colonne
        df = df.reset_index()  # Crée une colonne 'time'
        
        # Création des features (identiques au notebook d'entraînement)
        df["month"] = df["time"].dt.month
        df["year"] = df["time"].dt.year
        df["tavg_lag1"] = df["tavg"].shift(1)  # Température du mois précédent
        
        # Supprimer les lignes avec tavg_lag1 manquant
        df = df.dropna(subset=["tavg_lag1"]).reset_index(drop=True)
        
        if df.empty:
            st.error("""
            ❌ Après création de tavg_lag1, il ne reste plus de données utilisables.
            
            Cela peut arriver si vous avez moins de 2 mois de données.
            """)
            st.stop()
        
        # Préparer les données pour la prédiction
        last_row = df.iloc[-1]
        X_last = [[last_row["month"], last_row["year"], last_row["tavg_lag1"]]]
        
        # Faire la prédiction
        prediction = model.predict(X_last)[0]
        
        # Afficher le résultat
        st.success(f"### 🎯 Prévision tavg (mois suivant) ≈ **{prediction:.2f} °C**")
        st.caption(f"📊 Source des données: {source_used}")
        
        # Afficher les dernières données utilisées
        st.subheader("📋 Dernières données mensuelles (features)")
        display_cols = ["time", "month", "year", "tavg", "tavg_lag1"]
        available_cols = [col for col in display_cols if col in df.columns]
        st.dataframe(
            df[available_cols].tail(12).style.format({
                "tavg": "{:.2f}",
                "tavg_lag1": "{:.2f}"
            })
        )
        
        # Graphique de l'historique
        st.subheader("📈 Historique tavg (mensuel)")
        chart_data = df.set_index("time")["tavg"]
        st.line_chart(chart_data)
        
        # Statistiques supplémentaires
        with st.expander("📊 Statistiques détaillées"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Température moyenne", f"{df['tavg'].mean():.2f} °C")
            with col2:
                st.metric("Température min", f"{df['tavg'].min():.2f} °C")
            with col3:
                st.metric("Température max", f"{df['tavg'].max():.2f} °C")
            
            st.write(f"**Période des données:** {df['time'].min().strftime('%Y-%m')} à {df['time'].max().strftime('%Y-%m')}")
            st.write(f"**Nombre total de mois:** {len(df)}")

# Informations dans la sidebar
with st.sidebar:
    st.header("ℹ️ À propos")
    st.write("""
    Cette application utilise un modèle de régression linéaire 
    entraîné pour prédire la température moyenne du mois suivant 
    basée sur:
    - Le mois de l'année
    - L'année
    - La température du mois précédent
    """)
    
    st.header("📝 Instructions")
    st.write("""
    1. Entrez les coordonnées (latitude/longitude)
    2. Ajustez les paramètres si nécessaire
    3. Cliquez sur "Prédire le mois suivant"
    """)
    
    st.header("🌍 Exemples de localisation")
    if st.button("Dakar, Sénégal"):
        st.rerun()
    st.write("Lat: 14.7167, Lon: -17.4677")
    
    st.divider()
    st.caption("Données: Meteostat | Modèle: LinearRegression (scikit-learn)")
