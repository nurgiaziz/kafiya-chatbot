"""
Untuk menjalankan, lakukan di terminal

>>> streamlit run app1.py
"""

import streamlit as st

st.title("Applikasi Adib 😊")

st.markdown("Ini adalah aplikasi bikinan Adib")

user_name = st.text_input("Nama")
user_age = st.slider("Umur")
submit_button = st.button("Submit")
if submit_button:
    st.markdown(f"Hello {user_name}!")
    st.markdown(f"Umur {user_age} tahun")