import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# 1. Configuração do Firebase
if not firebase_admin._apps:
    try:
        # Carrega a string JSON do Secrets
        secret_json = st.secrets["FIREBASE_CREDENTIALS"]
        
        # Converte para dicionário
        config_dict = json.loads(secret_json)
        
        # Corrige a quebra de linha na chave privada (crucial para o erro ValueError)
        if "private_key" in config_dict:
            config_dict["private_key"] = config_dict["private_key"].replace('\\n', '\n')
            
        # Inicializa o Firebase
        cred = credentials.Certificate(config_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Erro ao inicializar Firebase: {e}")

# Inicializa o Firestore
db = firestore.client()

# 2. Configuração do Gemini
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error(f"Erro ao configurar Gemini: {e}")

st.title("Matriz Vitruviana")
st.success("Sistema carregado com sucesso!")
