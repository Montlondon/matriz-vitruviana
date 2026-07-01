import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import base64

if not firebase_admin._apps:
    # Decodifica e garante que a chave seja uma string limpa
    raw_key = base64.b64decode(st.secrets["FIREBASE_PRIVATE_KEY_BASE64"]).decode('utf-8').strip()
    
    # Criamos o certificado diretamente, sem transformar em dicionário intermediário que pode corromper
    cert = credentials.Certificate({
        "type": st.secrets["FIREBASE_TYPE"],
        "project_id": st.secrets["FIREBASE_PROJECT_ID"],
        "private_key_id": st.secrets["FIREBASE_PRIVATE_KEY_ID"],
        "private_key": raw_key,
        "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
        "client_id": st.secrets["FIREBASE_CLIENT_ID"],
        "auth_uri": st.secrets["FIREBASE_AUTH_URI"],
        "token_uri": st.secrets["FIREBASE_TOKEN_URI"],
        "auth_provider_x509_cert_url": st.secrets["FIREBASE_AUTH_PROVIDER_X509_CERT_URL"],
        "client_x509_cert_url": st.secrets["FIREBASE_CLIENT_X509_CERT_URL"]
    })
    
    firebase_admin.initialize_app(cert)

# ... resto do seu código
