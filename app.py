import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase
if not firebase_admin._apps:
    try:
        # Carrega a string JSON
        json_str = st.secrets["FIREBASE_CREDENTIALS"]
        # Converte para dicionário
        cred_dict = json.loads(json_str)
        # Corrige a quebra de linha da chave privada
        cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
        
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        st.error(f"Erro no Firebase: {e}")

# Inicializa o Firestore
db = firestore.client()

# Configuração do Gemini (agora separado)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Matriz Vitruviana")
st.success("Tudo carregado com sucesso!")
