import streamlit as st
import pandas as pd
import joblib

# CONFIG PAGE
st.set_page_config(
    page_title="Prédiction état de la valve",
    layout="centered"
)

st.title(" Prédiction de l’état de la valve")

st.write("""
Cette application permet de prédire l’état de la valve  
(**optimale / non optimale**) à partir d’un **numéro de cycle**.
""")

# CHARGEMENT DES OBJETS ML
model = joblib.load("svm_model.pkl")     
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# DONNÉES FEATURES
data = pd.read_csv("dataset_streamlit.csv", index_col=0)

# INPUT UTILISATEUR
cycle_id = st.number_input(
    "Entrer le numéro du cycle",
    min_value=int(data.index.min()),
    max_value=int(data.index.max()),
    step=1
)

# PREDICTION
if st.button("Prédire l'état de la valve"):

    if cycle_id not in data.index:
        st.error(" Cycle non trouvé dans les données.")
    else:
        
        X = data.loc[[cycle_id]]

        
        X = X[feature_names]

        # Normalisation
        X_scaled = scaler.transform(X)

        # Prédiction
        pred = model.predict(X_scaled)[0]
        proba = model.predict_proba(X_scaled)[0, 1]

        st.subheader("Résultat")

        if pred == 1:
            st.success(f" Valve OPTIMALE\n\nProbabilité : {proba:.2f}")
        else:
            st.error(f" Valve NON OPTIMALE\n\nProbabilité : {proba:.2f}")
