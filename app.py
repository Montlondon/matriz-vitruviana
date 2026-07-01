import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json

# Verifica se o app já foi inicializado
if not firebase_admin._apps:
    # Transformamos os segredos em um dicionário
    cred_dict = dict(st.secrets["FIREBASE"])
    
    # O Firebase espera que a chave privada contenha quebras de linha reais
    # O Streamlit às vezes interpreta o \n literalmente. Se der erro, tente:
    cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
    
    # Inicializa com o dicionário, não com o nome do arquivo
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
