import getpass
import os

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

api_key = getpass.getpass("Enter your API Key: ")
os.environ["GOOGLE_API_KEY"] = api_key
os.environ["GROQ_API_KEY"] = api_key

client = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
# client = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

print("LLM is ready!")
chat_history = [SystemMessage("You are a comedian")]

while True:
    prompt = input("User: ")
    print()
    chat_history.append(HumanMessage(prompt))
    response = client.invoke(chat_history)
    print("AI:", response.content)
    print()

