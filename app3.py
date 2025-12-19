"""
Untuk menjalankan:

>>> streamlit run app3.py
"""

import os

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


st.title("ChatBotKu")

# Check apakah API key sudah ada?
if "GROQ_API_KEY" not in os.environ:
    # Jika belum ada, minta API key, dan jangan tampilkan chatbot dulu
    groq_api_key = st.text_input("Groq API Key:", type="password")
    api_submit_button = st.button("Enter")
    if api_submit_button:
        os.environ["GROQ_API_KEY"] = groq_api_key
        st.rerun()
    st.stop()
# Jika sudah ada API key, tidak perlu minta lagi -> tampikan chatbot

# Bikin client untuk LLM
llm =  ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# Bikin chat history kosong jika belum ada di session state
if "chat_history" not in st.session_state:
    # Tambahkan system message seperlunya
    st.session_state["chat_history"] = [
        SystemMessage("You are a chatbot about cooking recipe. If you receive question not in this topic, you must say that you can't answer")
    ]

# Tampikan chat history yang ada sampai sekarang
for chat in st.session_state["chat_history"]:
    if type(chat) is SystemMessage:
        continue
    role = "User" if type(chat) is HumanMessage else "AI"
    with st.chat_message(role):
        st.markdown(chat.content)

# Minta input dari user
user_chat = st.chat_input("Chat with AI")
if not user_chat:
    # Jika belum ada input, stop tunggu sampai ada
    st.stop()

# Tampilkan input user jika sudah ada
with st.chat_message("User"):
    st.markdown(user_chat)

# Masukkan input user ke chat history
st.session_state["chat_history"].append(HumanMessage(user_chat))
# Kirim chat ke LLM, dapatkan respons LLM
response = llm.invoke(st.session_state["chat_history"])
# Masukkan respons LLM ke chat history
st.session_state["chat_history"].append(response)

# Tampilkan respons LLM
with st.chat_message("AI"):
    st.markdown(response.content)

