# No seu app.py, altere apenas a parte da private_key:
cred_dict = {
    "type": st.secrets["FIREBASE_TYPE"],
    "project_id": st.secrets["FIREBASE_PROJECT_ID"],
    "private_key_id": st.secrets["FIREBASE_PRIVATE_KEY_ID"],
    # O ajuste está aqui:
    "private_key": st.secrets["FIREBASE_PRIVATE_KEY"].encode('utf-8').decode('unicode_escape'),
    "client_email": st.secrets["FIREBASE_CLIENT_EMAIL"],
    "client_id": st.secrets["FIREBASE_CLIENT_ID"],
    "auth_uri": st.secrets["FIREBASE_AUTH_URI"],
    "token_uri": st.secrets["FIREBASE_TOKEN_URI"],
    "auth_provider_x509_cert_url": st.secrets["FIREBASE_AUTH_PROVIDER_CERT_URL"],
    "client_x509_cert_url": st.secrets["FIREBASE_CLIENT_CERT_URL"]
}
