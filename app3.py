"""
Untuk menjalankan:

>>> streamlit run app3.py
"""

import os

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


st.title("ChatBotKu")

if "GROQ_API_KEY" not in os.environ:
    groq_api_key = st.text_input("Groq API Key:", type="password")
    api_submit_button = st.button("Enter")
    if api_submit_button:
        os.environ["GROQ_API_KEY"] = groq_api_key
        st.rerun()
    st.stop()

llm =  ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

for chat in st.session_state["chat_history"]:
    role = "User" if type(chat) is HumanMessage else "AI"
    with st.chat_message(role):
        st.markdown(chat.content)

user_chat = st.chat_input("Chat with AI")
if not user_chat:
    st.stop()

with st.chat_message("User"):
    st.markdown(user_chat)

st.session_state["chat_history"].append(HumanMessage(user_chat))
response = llm.invoke(st.session_state["chat_history"])
st.session_state["chat_history"].append(response)

with st.chat_message("AI"):
    st.markdown(response.content)

