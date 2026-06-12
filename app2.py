# Jalankan dengan
# >>> streamlit run <nama file>
#
# Atau
# >>> python -m streamlit run <nama file>
#

import os

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

st.title("My ChatBot")
st.markdown("Demo chatbot oleh Mukhlas Adib")

# Inisialisasi API Key kosong untuk pertama kali
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

# Tampilkan input API key juga key belum ada
if st.session_state["api_key"] == "":
    input_api_key = st.text_input("API Key", type="password")
    submit_key = st.button("Submit Key")
    # Simplan API key hanya jika tombol submit ditekan
    if submit_key:
        st.session_state["api_key"] = input_api_key
    if st.session_state["api_key"] != "":
        st.rerun()
    # Jangan tampilkan lainnya jika API key belum ada
    st.stop()
# Dari sini, hanya akan dirender jika API key sudah ada

# Register API key ke env variable
os.environ["GOOGLE_API_KEY"] = st.session_state["api_key"]
os.environ["GROQ_API_KEY"] = st.session_state["api_key"]

# Bikin client LLM
client = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
# client = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Inisialisasi chat history dengan system message untuk pertama kali
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [SystemMessage("You are a funny comedian.")]

# Display chat history bubble sampai sekarang
for chat in st.session_state["chat_history"]:
    if type(chat) is HumanMessage:
        role = "human"
    elif type(chat) is SystemMessage:
        # Jangan tampilkan system prompt
        continue
    else:
        role = "ai"
    with st.chat_message(role):
        st.markdown(chat.content)

# Minta input chat dari user
user_input = st.chat_input("Chat here")
if not user_input:
    st.stop()

# Tambahkan input user ke history, dan langsung tampilkan di bubble
st.session_state["chat_history"].append(HumanMessage(user_input))
with st.chat_message("human"):
    st.markdown(st.session_state["chat_history"][-1].content)

# Jalankan LLM, dan rerun semuanya agar output LLM masuk ke bubble
response = client.invoke(st.session_state["chat_history"])
st.session_state["chat_history"].append(response)
st.rerun()
