import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase
if not firebase_admin._apps:
    try:
        secret_json = st.secrets["FIREBASE_CREDENTIALS"]
        config_dict = json.loads(secret_json)
        
        # Corrige a quebra de linha forçadamente
        if "private_key" in config_dict:
            # Substitui a representação literal de nova linha por caracteres de quebra reais
            config_dict["private_key"] = config_dict["private_key"].replace("\\n", "\n")
            
        cred = credentials.Certificate(config_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Erro ao inicializar Firebase: {e}")

# Inicializa o Firestore com verificação
try:
    if firebase_admin._apps:
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
st.success("Sistema carregado com sucesso.")
