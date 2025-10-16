import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

MESSAGE_ROLE = {
    HumanMessage: "User",
    AIMessage: "Assistant",
}


def display_one_message(message):
    role = MESSAGE_ROLE[type(message)]
    with st.chat_message(role):
        st.markdown(message.content)


if "google_api_key" not in st.session_state or not st.session_state["google_api_key"]:
    api_key = st.text_input("🔑 Enter your Google AI API Key", type="password")
    if api_key:
        st.session_state["google_api_key"] = api_key
        st.rerun()
    else:
        st.stop()


if "llm" not in st.session_state:
    st.session_state["llm"] = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", google_api_key=st.session_state["google_api_key"]
    )
llm = st.session_state["llm"]


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
chat_history = st.session_state["chat_history"]


for msg in chat_history:
    display_one_message(msg)


user_prompt = st.chat_input("Type your message here...")
if not user_prompt:
    st.stop()
chat_history.append(HumanMessage(content=user_prompt))
display_one_message(chat_history[-1])


response = llm.invoke(chat_history)
chat_history.append(response)
display_one_message(chat_history[-1])
