import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# 1. Configuração do Firebase
if not firebase_admin._apps:
    # Lê a credencial do Streamlit Secrets
    firebase_config = json.loads(st.secrets["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. Configuração do Gemini
genai.configure(api_key=st.secrets["AQ.Ab8RN6IfcYpb6eMRhthSmUF5zVAEdrMkn0oZOpuN3nJu4aDDvA"])

# 3. Restante do seu código da Matriz Vitruviana abaixo...
st.title("Matriz Vitruviana")
# ... (seu código continua aqui)
