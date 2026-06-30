import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# 1. Configuração do Firebase
if not firebase_admin._apps:
    # Lê a string do Secrets que contém o JSON
    config_json = st.secrets["FIREBASE_CREDENTIALS"]
    config_dict = json.loads(config_json)
    
    # Inicializa o Firebase
    cred = credentials.Certificate(config_dict)
    firebase_admin.initialize_app(cred)

# Inicializa o Firestore
db = firestore.client()

# 2. Configuração do Gemini
# Certifique-se de que no Secrets você tem: GOOGLE_API_KEY = "sua_chave"
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Matriz Vitruviana - Conectado!")
st.success("Firebase e Gemini inicializados com sucesso.")
