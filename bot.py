import os
import json
import random
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_random_hadith():
    with open("riyad_assalihin.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    hadith = random.choice(data["hadiths"])

    return hadith["arabic"]

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

if __name__ == "__main__":
    hadith_text = get_random_hadith()
    send_telegram_message(hadith_text)