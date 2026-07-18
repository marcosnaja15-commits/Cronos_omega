import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="CRONOS", layout="centered")

if "chat" not in st.session_state:
    genai.configure(api_key=st.secrets["API_KEY"])
    st.session_state.chat = genai.GenerativeModel('gemini-1.5-flash').start_chat(history=[])

st.title("⚡ CRONOS | OPERACIONAL")
if prompt := st.chat_input("Comando:"):
    resp = st.session_state.chat.send_message(prompt)
    st.markdown(resp.text)
