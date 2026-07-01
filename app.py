import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai

# Inicialização segura do Firebase
if not firebase_admin._apps:
    try:
        # Montamos o dicionário a partir de chaves individuais no Secrets
        cred_dict = {
            "type": st.secrets["FIREBASE_TYPE"],
            "project_id": st.secrets["FIREBASE_PROJECT_ID"],
            "private_key_id": st.secrets["FIREBASE_PRIVATE_KEY_ID"],
            "private_key": st.secrets["FIREBASE_PRIVATE_KEY"].replace("\\n", "\n"),
            "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
            "client_id": st.secrets["FIREBASE_CLIENT_ID"],
            "auth_uri": st.secrets["FIREBASE_AUTH_URI"],
            "token_uri": st.secrets["FIREBASE_TOKEN_URI"],
            "auth_provider_x509_cert_url": st.secrets["FIREBASE_AUTH_PROVIDER_CERT_URL"],
            "client_x509_cert_url": st.secrets["FIREBASE_CLIENT_CERT_URL"]
        }
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)
        st.success("Firebase conectado!")
    except Exception as e:
        st.error(f"Erro no Firebase: {e}")

# Inicializa o Firestore
db = firestore.client()

# Configuração do Gemini
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
st.success("Gemini configurado!")

st.title("Matriz Vitruviana")
