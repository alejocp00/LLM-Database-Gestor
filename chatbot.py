from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from lib.history import History

# Load envs
load_dotenv()

# Initialize OpenAI API
model = ChatOpenAI(model="gpt-3.5-turbo")

# # Streamlit app
st.title("Generate sql schemas with prompts")

# Initialize chat history
history = History()

# Display chat messages from history on app rerun
for message in history.get():
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):

  # Display user message in chat message container
  with st.chat_message("user"):
    st.markdown(prompt)    
  
  # Add user message to chat history
  history.add("user", prompt)
  
  # Get llm answer
  response = model.invoke(history.get(chat=True))
  with st.chat_message("assistant"):
    st.markdown(response.content)

  history.add("assistant", response.content)
  