# modules/text_to_image.py
import os
import base64
import google.generativeai as genai
from PIL import Image
from io import BytesIO
import uuid


genai.configure(api_key="AIzaSyC9-vsBPIgub5wmC0EzwDVt1YrvcGIt2fo")

def generate_image(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro-vision")
    try:
        response = model.generate_content(prompt, stream=False)
        if response and response.parts:
            # Just saving the text response as an image
            img_text = response.parts[0].text
            image = Image.new("RGB", (800, 200), color=(255, 255, 255))
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), img_text, fill=(0, 0, 0))
            file_path = f"gemini_text_{uuid.uuid4().hex[:6]}.png"
            image.save(file_path)
            return file_path
        else:
            return ""
    except Exception as e:
        print(f"[Gemini Error]: {e}")
        return ""
