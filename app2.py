# Jalankan dengan
# >>> streamlit run <nama file>
#
# Atau
# >>> python -m streamlit run <nama file>
#

import getpass
import os
from inspect import markcoroutinefunction

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

st.title("My ChatBot")
st.markdown("Demo chatbot oleh Mukhlas Adib")

if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

if st.session_state["api_key"] == "":
    input_api_key = st.text_input("API Key", type="password")
    submit_key = st.button("Submit Key")
    if submit_key:
        st.session_state["api_key"] = input_api_key
    if st.session_state["api_key"] != "":
        st.rerun()
    st.stop()

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

for chat in st.session_state["chat_history"]:
    if type(chat) is HumanMessage:
        role = "human"
    else:
        role = "ai"
    with st.chat_message(role):
        st.markdown(chat.content)

user_input = st.chat_input("Chat here")
if not user_input:
    st.stop()

st.session_state["chat_history"].append(HumanMessage(user_input))
if user_input:
    st.rerun()
