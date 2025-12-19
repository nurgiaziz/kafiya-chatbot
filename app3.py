"""
Untuk menjalankan:

>>> streamlit run app3.py
"""
import os

import streamlit as st

st.title("ChatBotKu")

if "GROQ_API_KEY" not in os.environ:
    groq_api_key = st.text_input("Groq API Key:", type="password")
    api_submit_button = st.button("Enter")
    if api_submit_button:
        os.environ["GROQ_API_KEY"] = groq_api_key
        st.rerun()
    st.stop()

st.markdown("API Key sudah ada!, Silahkan lanjut")
