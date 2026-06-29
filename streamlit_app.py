import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import google.generativeai as genai

# 1. Configuração do Firebase
if not firebase_admin._apps:
    # IMPORTANTE: Verifique se o nome do arquivo JSON está exato na sua pasta
    cred = credentials.Certificate('projeto-firebase-xxxx.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. Configuração do Gemini
# Cole sua chave real (a que termina em ...DDvA) aqui:
genai.configure(api_key='AQ.Ab8RN6IfcYpb6eMRhthSmUF5zVAEdrMkn0oZOpuN3nJu4aDDvA') 

# Usamos o modelo 'gemini-1.5-flash' diretamente
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Interface Principal
st.title("Matriz Vitruviana - Núcleo de IA")

menu = st.sidebar.selectbox("Menu", ["Registro", "Consultar"])

if menu == "Registro":
    st.subheader("Cadastro de Paciente")
    nome = st.text_input("Nome")
    queixa = st.text_area("Queixa")
    if st.button("Registrar"):
        if nome and queixa:
            db.collection("Pacientes").add({"nome": nome, "queixa": queixa})
            st.success("Registrado com sucesso!")

elif menu == "Consultar":
    st.subheader("Análise Clínica")
    
    # Busca no Firestore
    pacientes = db.collection("Pacientes").stream()
    
    for p in pacientes:
        dados = p.to_dict()
        with st.expander(f"Paciente: {dados.get('nome')}"):
            st.write(f"Queixa: {dados.get('queixa')}")
            
            # Usamos o ID do documento como chave para o botão
            if st.button(f"Analisar {dados.get('nome')}", key=p.id):
                try:
                    with st.spinner('Analisando...'):
                        # Chamada simples e direta
                        response = model.generate_content(f"Como acupunturista, analise: {dados.get('queixa')}")
                        st.info(response.text)
                except Exception as e:
                    st.error(f"Erro na IA: {e}")