"""
Cara jalankan:

>>> python app2.py
"""

import os
import getpass

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

GROQ_API_KEY = getpass.getpass("Enter your API key: ")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

llm =  ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

chat_history = []

print("Silahkan chat dengan AI anda!!!")
while True:
    user_chat = input("User: ")
    chat_history.append(
        HumanMessage(user_chat)
    )
    response = llm.invoke(chat_history)
    chat_history.append(response)
    print(response.content)