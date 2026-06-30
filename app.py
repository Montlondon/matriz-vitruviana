import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Carregar Firebase com segurança
if not firebase_admin._apps:
    # Esta linha busca a string que você salvou no "Secrets"
    config_dict = json.loads(st.secrets["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(config_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Configuração do Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
