# Jalankan dengan
# >>> streamlit run <nama file>
#
# Atau
# >>> python -m streamlit run <nama file>
#

import streamlit as st

st.title("My ChatBot")
st.markdown("Demo chatbot oleh Mukhlas Adib")

if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

if st.session_state["api_key"] == "":
    input_api_key = st.text_input("API Key", type="password")
    submit_key = st.button("Submit Key")
    if submit_key:
        st.session_state["api_key"] = input_api_key
    if st.session_state["api_key"] == "":
        st.stop()

st.markdown("Chatbot is ready!")
