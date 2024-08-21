import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Initialize Gemini-Pro 
GOOGLE_GEMINI_KEY = "AIzaSyAsK0m7zG44ybiRqR_5-2XAYjrXURdRREo"
genai.configure(api_key=GOOGLE_GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title

#img = Image.open("OIP.jpeg") 
st.title("AI Chatbot")
# Create columns layout


# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("Enter your need.."):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Send user entry to Gemini and read the response
    response = st.session_state.chat.send_message(prompt) 
    
    # Display last 
    with st.chat_message("assistant"):
        st.markdown(response.text)


