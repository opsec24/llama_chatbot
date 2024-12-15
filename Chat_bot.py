#import streamLit package
#import langchain packages


import streamlit as st
 
from langchain_ollama import ChatOllama
from langchain_core.prompts import ( SystemMessagePromptTemplate,
                                    HumanMessagePromptTemplate,
                                    ChatMessagePromptTemplate,
                                    MessagesPlaceholder)

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory

from langchain_core.output_parsers import StrOutputParser



st.title("Welcome to the chat")
st.write("Private Chat bot ! Privacy and security")

base_url = "http://localhost:11434"
model  = 'llama3.2:3b'

st.chat_input("Write your message")