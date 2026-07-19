
import streamlit as st
import google.generativeai as genai

st.title("Cronos_omega")

# Conecta com a chave que você salvou no site
key = st.secrets.get("GOOGLE_API_KEY")
if key:
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    
    # Caixa simples para digitar
    pergunta = st.text_input("O que a Mente de Elite deve processar?")
    if st.button("Enviar"):
        if pergunta:
            resposta = model.generate_content(pergunta)
            st.write(resposta.text)
        else:
            st.warning("Digite algo primeiro.")
else:
    st.error("A chave da API não foi encontrada no site. Verifique o campo Secrets.")
