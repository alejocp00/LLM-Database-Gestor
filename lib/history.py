import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

class History:
  def __init__(self):
    if "history" not in st.session_state:
      st.session_state.history = []
    
  def add(self, role: str, content: str):
    st.session_state.history.append({
      "role": role,
      "content": content
    })
    
  def get(self, amount = "all", chat = False):
    messages = []
    if amount == "all":
      messages = st.session_state.history
    else:
      messages = st.session_state.history[-amount]
    
    if chat is False:
      return messages
    
    return [
      HumanMessage(content=m["content"]) if m["role"] == "user"
      else AIMessage(content=m["content"])
      for m in messages
    ]