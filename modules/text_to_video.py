# modules/text_to_video.py
import os
import requests
import uuid

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/damo-vilab/modelscope-text-to-video-synthesis"

def generate_video(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        filename = f"video_{uuid.uuid4().hex[:6]}.mp4"
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        print("Video generation failed:", response.status_code, response.text)
        return ""
