import os

import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("My ChatBot")

google_api_key = st.text_input("Google API Key", type="password")
os.environ["GOOGLE_API_KEY"] = google_api_key


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

user_query = st.text_input("Your query:")
submit = st.button("Submit")

response = None
if submit:
    messages_history: list = [
        SystemMessage(
            "You are a comedian that knows a lot about Bali. Always response in less than 3 sentences in a chat style. Reply in bahasa indonesia"
        )
    ]
    messages_history.append(HumanMessage(user_query))
    response = llm.invoke(messages_history)

if response is not None:
    st.write(f"AI: {response.content}")
