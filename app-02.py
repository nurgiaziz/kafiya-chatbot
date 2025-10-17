import streamlit as st

st.title("ChatBot-Ku")

st.write("ChatBot bikinan Adib")

GOOGLE_API_KEY = st.text_input("Google API Key")
is_submit_pressed = st.button("Submit")
if is_submit_pressed:
    st.write("API KEY Adalah", GOOGLE_API_KEY)
