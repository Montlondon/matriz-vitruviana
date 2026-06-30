import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase
if not firebase_admin._apps:
    try:
        # Pega a string do Secrets
        secret_json = st.secrets["FIREBASE_CREDENTIALS"]
        config_dict = json.loads(secret_json)
        
        # CORREÇÃO: Força a substituição de quebras de linha literais por quebras reais
        pk = config_dict["private_key"]
        pk = pk.replace("\\n", "\n")
        config_dict["private_key"] = pk
            
        cred = credentials.Certificate(config_dict)
        firebase_admin.initialize_app(cred)
        st.success("Firebase inicializado com sucesso!")
    except Exception as e:
        st.error(f"Erro na inicialização do Firebase: {e}")

# Inicializa o Firestore
try:
    db = firestore.client()
except Exception as e:
    st.error(f"Erro ao conectar no Firestore: {e}")

# Configuração do Gemini
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.success("Gemini configurado!")
except Exception as e:
    st.error(f"Erro no Gemini: {e}")

st.title("Matriz Vitruviana")
st.write("Sistema carregado.")
