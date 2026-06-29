import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai
import json

# Inicializa o Firebase de forma segura
if not firebase_admin._apps:
    config_dict = json.loads(st.secrets["FIREBASE_CREDENTIALS"])
    cred = credentials.Certificate(config_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Inicializa o Gemini
genai.configure(api_key=st.secrets["AQ.Ab8RN6IfcYpb6eMRhthSmUF5zVAEdrMkn0oZOpuN3nJu4aDDvA"])

# A partir daqui, seu código continua normalmente...
