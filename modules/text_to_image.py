# modules/text_to_image.py
import os
import base64
import google.generativeai as genai
from PIL import Image
from io import BytesIO
import uuid

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def generate_image(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro-vision")

    try:
        response = model.generate_content(prompt, stream=False)
        if response and response.parts:
            img_data = response.parts[0].text
            image_bytes = base64.b64decode(img_data)
            image = Image.open(BytesIO(image_bytes))
            file_path = f"gemini_img_{uuid.uuid4().hex[:6]}.png"
            image.save(file_path)
            return file_path
        else:
            return ""
    except Exception as e:
        print(f"[Gemini Error]: {e}")
        return ""
