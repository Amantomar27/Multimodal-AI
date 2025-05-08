# modules/company_chatbot.py
import streamlit as st
import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv("AIzaSyC9-vsBPIgub5wmC0EzwDVt1YrvcGIt2fo")
genai.configure(api_key=GOOGLE_API_KEY)

def company_chat_interface():
    st.subheader("🤖 Company Custom Chatbot")

    # Predefined company-related details
    company_info = """
    Insular is a tech-driven company specializing in innovative blockchain solutions.
    We aim to optimize business workflows through distributed ledger technology and smart contracts.
    Our team is passionate about pushing the boundaries of decentralized applications (dApps) and secure digital platforms.
    """

    st.write("Company Overview: ")
    st.write(company_info)

    user_query = st.text_input("Ask the Company Chatbot about our services:")

    if user_query:
        model = genai.GenerativeModel("gemini-pro")
        
        try:
            with st.spinner("Generating response..."):
                # Respond to company-specific queries
                response = model.generate_content([user_query, company_info], stream=False)
                st.success("Response from Company Chatbot:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
