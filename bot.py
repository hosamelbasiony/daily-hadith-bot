import os
import json
import random
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS")  # comma separated

def get_random_hadith():
    with open("riyad_assalihin.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    hadith = random.choice(data["hadiths"])
    return hadith["arabic"]

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    chat_ids = [chat_id.strip() for chat_id in CHAT_IDS.split(",")]

    for chat_id in chat_ids:
        payload = {
            "chat_id": chat_id,
            "text": text
        }
        response = requests.post(url, data=payload)

        if response.status_code != 200:
            print(f"Failed to send to {chat_id}: {response.text}")

if __name__ == "__main__":
    hadith_text = get_random_hadith()
    send_telegram_message(hadith_text)