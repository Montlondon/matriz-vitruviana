import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Função para inicializar o Firebase com segurança
def initialize_firebase():
    if not firebase_admin._apps:
        try:
            # Carrega o JSON dos segredos
            secret_json = st.secrets["FIREBASE_CREDENTIALS"]
            
            # Se for uma string, faz o parsing para dicionário
            if isinstance(secret_json, str):
                cred_dict = json.loads(secret_json)
            else:
                cred_dict = dict(secret_json)

            # --- CORREÇÃO DO ERRO INVALIDBYTE ---
            # Forçamos a substituição do caractere literal '\n' por uma quebra de linha real
            if "private_key" in cred_dict:
                cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            
            # Inicializa com o dicionário corrigido
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            st.success("Firebase inicializado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao inicializar Firebase: {e}")

# Executa a inicialização
initialize_firebase()
db = firestore.client()

st.title("Matriz Vitruviana")
