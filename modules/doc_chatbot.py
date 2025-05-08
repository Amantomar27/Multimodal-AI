# modules/doc_chatbot.py
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def doc_chat_interface():
    st.subheader("📄 Document Chatbot (Image-based)")
    
    uploaded_file = st.file_uploader("Upload a document image (JPG/PNG)", type=["png", "jpg", "jpeg"])
    question = st.text_input("Ask a question about the document")

    if uploaded_file and question:
        image = Image.open(uploaded_file)
        model = genai.GenerativeModel("gemini-pro-vision")
        
        try:
            with st.spinner("Analyzing document and generating answer..."):
                response = model.generate_content([question, image], stream=False)
                st.success("Answer:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
