import os

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
chat_history = st.session_state["chat_history"]

st.title("ChatBot-Ku")


def get_api_key_input():
    st.write("Masukkan Google API Key")

    if "GOOGLE_API_KEY" not in st.session_state:
        st.session_state["GOOGLE_API_KEY"] = ""

    col1, col2 = st.columns((80, 20))
    with col1:
        api_key = st.text_input("", label_visibility="collapsed", type="password")

    with col2:
        is_submit_pressed = st.button("Submit")
        if is_submit_pressed:
            st.session_state["GOOGLE_API_KEY"] = api_key

    os.environ["GOOGLE_API_KEY"] = st.session_state["GOOGLE_API_KEY"]


def load_llm():
    if "llm" not in st.session_state:
        st.session_state["llm"] = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    return st.session_state["llm"]


get_api_key_input()
if not os.environ["GOOGLE_API_KEY"]:
    st.stop()

llm = load_llm()

prompt = st.chat_input("Chat with AI")
chat_history.append(prompt)
for chat in chat_history:
    with st.chat_message("User"):
        st.markdown(chat)
