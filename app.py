import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai

# Carregar credenciais de forma robusta
try: 
    if not firebase_admin._apps:
        # Criamos o dicionário buscando apenas o que o Streamlit reconhece como segredo
        cred_dict = {
            "type": st.secrets["FIREBASE_TYPE"],
            "project_id": st.secrets["FIREBASE_PROJECT_ID"],
            "private_key_id": st.secrets["FIREBASE_PRIVATE_KEY_ID"],
            "private_key": st.secrets["FIREBASE_PRIVATE_KEY"].replace("\\n", "\n"),
            "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
            "client_id": st.secrets["FIREBASE_CLIENT_ID"],
            "auth_uri": st.secrets["FIREBASE_AUTH_URI"],
            "token_uri": st.secrets["FIREBASE_TOKEN_URI"],
            "auth_provider_x509_cert_url": st.secrets["FIREBASE_AUTH_PROVIDER_X509_CERT_URL"],
            "client_x509_cert_url": st.secrets["FIREBASE_CLIENT_X509_CERT_URL"]
        }
        firebase_admin.initialize_app(credentials.Certificate(cred_dict))
    
    db = firestore.client()
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    st.title("Matriz Vitruviana")
    st.success("Conectado com sucesso!")

except KeyError as e:
    st.error(f"Erro: A chave {e} não foi encontrada no 'Secrets'. Verifique se todos os nomes estão exatamente iguais.")
except Exception as e:
    st.error(f"Erro inesperado: {e}")
