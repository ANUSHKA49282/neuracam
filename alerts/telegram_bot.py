# alerts/telegram_bot.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_alert(message="🚨 NeuraCam Alert: Suspicious activity detected!"):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        print("📨 Text alert sent:", response.text)
    except Exception as e:
        print("❌ Error sending text:", e)

def send_telegram_photo(image_path, caption="📸 Snapshot from NeuraCam"):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(image_path, "rb") as photo:
            data = {"chat_id": CHAT_ID, "caption": caption}
            files = {"photo": photo}
            response = requests.post(url, data=data, files=files)
            print("📷 Photo alert sent:", response.text)
    except Exception as e:
        print("❌ Error sending photo:", e)
