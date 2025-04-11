'''import streamlit as st
import requests

st.title("📊 Rapport de Performance du Troupeau")
API_URL = "http://localhost:8000"

if st.button("Générer un nouveau rapport"):
    response = requests.post(f"{API_URL}/generate-report")
    if response.status_code == 200:
        report_url = response.json()["report_url"]
        st.success(f"Rapport généré ! [Télécharger ici]({API_URL}{report_url})")
    else:
        st.error("Erreur lors de la génération du rapport")

st.title("📊 Rapport de Performance du Troupeau")
API_URL = "http://localhost:8000"

if st.button("Générer un nouveau rapport"):
    response = requests.post(f"{API_URL}/generate-report")
    if response.status_code == 200:
        report_url = response.json()["report_url"]
        st.success(f"Rapport généré ! [Télécharger ici]({API_URL}{report_url})")
    else:
        st.error("Erreur lors de la génération du rapport")'''

import streamlit as st
import requests

st.title("📊 Rapport de Performance du Troupeau")
API_URL = "http://localhost:8000"

# ✅ Clé unique ajoutée
if st.button("Générer un nouveau rapport", key="generate_report_btn"):
    try:
        response = requests.post(f"{API_URL}/generate-report")
        if response.status_code == 200:
            report_url = response.json()["report_url"]
            st.success(f"Rapport généré ! [Télécharger ici]({API_URL}{report_url})")
        else:
            st.error("Erreur lors de la génération du rapport")
    except Exception as e:
        st.error(f"Échec : {str(e)}")


