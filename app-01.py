import getpass
import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = getpass.getpass("Enter your API key: ")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage(content="You are a funny assistant that always joking."),
]

prompt = input("User: ")
messages.append(HumanMessage(content=prompt))
response = llm.invoke(messages)
print("AI:", response.content)
