import streamlit as st

if "GOOGLE_API_KEY" not in st.session_state:
    st.session_state["GOOGLE_API_KEY"] = ""
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
chat_history = st.session_state["chat_history"]

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

prompt = st.chat_input("Chat with AI")
chat_history.append(prompt)
for chat in chat_history:
    with st.chat_message("User"):
        st.markdown(chat)
