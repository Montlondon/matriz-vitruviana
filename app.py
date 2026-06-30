import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Configuração Firebase com limpeza rigorosa
if not firebase_admin._apps:
    try:
        # Carrega o segredo do Streamlit
        secret_json = st.secrets["FIREBASE_CREDENTIALS"]
        config_dict = json.loads(secret_json)
        
        # Corrige a chave privada: transforma a string literal '\n' em quebra de linha real
        # e remove caracteres estranhos
        pk = config_dict["private_key"]
        pk = pk.replace("\\n", "\n")
        config_dict["private_key"] = pk
            
        cred = credentials.Certificate(config_dict)
        firebase_admin.initialize_app(cred)
        st.success("Conexão Firebase realizada!")
    except Exception as e:
        st.error(f"Erro no Firebase: {e}")

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
st.write("Sistema carregado com sucesso.")
