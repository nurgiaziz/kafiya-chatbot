import streamlit as st

if "GOOGLE_API_KEY" not in st.session_state:
    st.session_state["GOOGLE_API_KEY"] = ""

st.title("ChatBot-Ku")

st.write("Masukkan Google API Key")

col1, col2 = st.columns((80, 20))
with col1:
    api_key = st.text_input("", label_visibility="collapsed")

with col2:
    is_submit_pressed = st.button("Submit")
    if is_submit_pressed:
        st.session_state["GOOGLE_API_KEY"] = api_key

GOOGLE_API_KEY = st.session_state["GOOGLE_API_KEY"]
st.write("API KEY Adalah", GOOGLE_API_KEY)

st.button("Random Button")
