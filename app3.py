import os

import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("My ChatBot")

google_api_key = st.text_input("Google API Key", type="password")
os.environ["GOOGLE_API_KEY"] = google_api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


if "messages_history" not in st.session_state:
    st.session_state["messages_history"] = [
        SystemMessage(
            "You are a comedian that knows a lot about Bali. Always response in less than 3 sentences in a chat style. Reply in bahasa indonesia"
        )
    ]
messages_history = st.session_state["messages_history"]

for message in messages_history:
    if type(message) is SystemMessage:
        continue
    role = "User" if type(message) is HumanMessage else "AI"
    with st.chat_message(role):
        st.markdown(message.content)

prompt = st.chat_input("Chat with AI")
if not prompt:
    st.stop()
messages_history.append(HumanMessage(prompt))
with st.chat_message("User"):
    st.markdown(prompt)

response = llm.invoke(messages_history)
messages_history.append(response)
with st.chat_message("AI"):
    st.markdown(response.content)
