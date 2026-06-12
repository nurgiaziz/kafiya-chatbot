# Jalankan dengan
# >>> streamlit run <nama file>
#
# Atau
# >>> python -m streamlit run <nama file>
#

import streamlit as st

st.title("My ChatBot")
st.markdown("Demo chatbot oleh Mukhlas Adib")

api_key = st.text_input("API Key", type="password")
submit_key = st.button("Submit Key")
if submit_key:
    st.markdown("We are ready!")
