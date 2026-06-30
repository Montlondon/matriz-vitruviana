import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase
if not firebase_admin._apps:
    try:
        # A MUDANÇA: Carregamos o segredo como um dicionário diretamente
        # O Streamlit já faz o parse automático do JSON se você colocar a estrutura correta
        key_dict = st.secrets["FIREBASE_CREDENTIALS"]
        
        # O truque: garante que a chave privada seja processada com quebras reais
        # Se você colou o JSON como uma string, convertemos agora:
        if isinstance(key_dict, str):
            key_dict = json.loads(key_dict)
            
        cred = credentials.Certificate(key_dict)
        firebase_admin.initialize_app(cred)
        st.success("Firebase conectado!")
    except Exception as e:
        st.error(f"Erro no Firebase: {e}")

# Inicializa o Firestore
db = firestore.client()

# Configuração do Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Matriz Vitruviana")
st.success("Sistema carregado com sucesso.")
