import streamlit as st

st.title("ChatBot-Ku")

st.write("ChatBot bikinan Adib")

col1, col2 = st.columns((80, 20))
with col1:
    GOOGLE_API_KEY = st.text_input("")

with col2:
    is_submit_pressed = st.button("Submit")

if is_submit_pressed:
    st.write("API KEY Adalah", GOOGLE_API_KEY)
