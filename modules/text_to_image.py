# modules/text_to_image.py
import os
from PIL import Image, ImageDraw
from io import BytesIO
import uuid
import google.generativeai as genai

genai.configure(api_key="AIzaSyC9-vsBPIgub5wmC0EzwDVt1YrvcGIt2fo")

def generate_image(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro-vision")

    try:
        response = model.generate_content(prompt, stream=False)
        if response and response.parts:
            text = response.parts[0].text

            # Create an image from the response text
            image = Image.new("RGB", (800, 300), color="white")
            draw = ImageDraw.Draw(image)
            draw.text((10, 10), text, fill="black")

            file_path = f"generated_img_{uuid.uuid4().hex[:6]}.png"
            image.save(file_path)
            return file_path
        else:
            return ""
    except Exception as e:
        print(f"[Gemini Error]: {e}")
        return ""
