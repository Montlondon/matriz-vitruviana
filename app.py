import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase com tratamento de erro robusto
if not firebase_admin._apps:
    try:
        secret_json = st.secrets["FIREBASE_CREDENTIALS"]
        config_dict = json.loads(secret_json)
        
        # Limpeza e correção da chave privada
        pk = config_dict["private_key"]
        pk = pk.replace("\\n", "\n")
        config_dict["private_key"] = pk
            
        cred = credentials.Certificate(config_dict)
        firebase_admin.initialize_app(cred)
        st.write("Conexão Firebase realizada!")
    except Exception as e:
        st.error(f"Erro no Firebase: {e}")

# Inicializa o Firestore
db = firestore.client()

# Configuração do Gemini
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.write("Gemini configurado!")
except Exception as e:
    st.error(f"Erro no Gemini: {e}")

st.title("Matriz Vitruviana")
st.success("Tudo carregado corretamente.")
