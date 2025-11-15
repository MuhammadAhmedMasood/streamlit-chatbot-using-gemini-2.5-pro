# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 14:22:17 2025

@author: DIZZLER
"""


        
#import google.generativeai as genai
#genai.configure(api_key="<your_api_key>")

#for m in genai.list_models():
 #   print(m.name)
 
import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with rehnuma!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-2.5-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Rehnuma - ChatBot")

st.markdown("""
    <div style="
        padding: 15px;
        border-radius: 12px;
        background: #f0f2f6;
        border: 1px solid #e0e0e0;
        margin-top: -10px;
        margin-bottom: 20px;">
        <h4 style="color:#4b4b4b; margin:0;">
            Your personal guide ✨ 
        </h4>
        <p style="color:#6b6b6b; margin-top:6px;">
            Ask anything. Rehnuma understands context and remembers the conversation.
        </p>
    </div>
""", unsafe_allow_html=True)


# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Rehnuma...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)




    




