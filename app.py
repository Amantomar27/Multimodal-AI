# app.py
import streamlit as st
from modules.text_to_image import generate_image
from modules.text_to_video import generate_video
from modules.doc_chatbot import doc_chat_interface
from modules.company_chatbot import company_chat_interface

st.set_page_config(page_title="Multi-Modal AI Platform", layout="wide")
st.title("🚀 Multi-Modal AI App: Text/Image/Video/Chat")

option = st.sidebar.selectbox("Choose Module", (
    "Text to Image", "Text to Video", "Document Chatbot", "Company Chatbot"
))

if option == "Text to Image":
    prompt = st.text_input("Enter image prompt")
    if st.button("Generate Image") and prompt:
        with st.spinner("Generating image using Gemini..."):
            img_path = generate_image(prompt)
            if img_path:
                st.image(img_path, caption="Generated Image")
            else:
                st.error("Image generation failed.")

elif option == "Text to Video":
    prompt = st.text_input("Enter video prompt")
    if st.button("Generate Video") and prompt:
        video_path = generate_video(prompt)
        if video_path:
            st.video(video_path)
        else:
            st.error("Video generation failed.")

elif option == "Document Chatbot":
    doc_chat_interface()

elif option == "Company Chatbot":
    company_chat_interface()
