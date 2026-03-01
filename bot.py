import os
import re
import json
import random
import requests
from dotenv import load_dotenv


# Load .env into environment (no-op if not present)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# Support CHAT_IDS (comma/semicolon/space-separated) or single CHAT_ID fallback
_chat_ids_env = os.getenv("CHAT_IDS") or os.getenv("CHAT_ID") or ""
CHAT_IDS = [c.strip() for c in re.split(r'[,;\s]+', _chat_ids_env) if c.strip()]


def get_random_hadith():
    with open("riyad_assalihin.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    hadith = random.choice(data["hadiths"])
    return hadith.get("arabic") or hadith.get("text") or str(hadith)


def send_telegram_message(text):
    if not CHAT_IDS:
        print("No CHAT_IDS or CHAT_ID configured; nothing to send")
        return
    if not BOT_TOKEN:
        print("BOT_TOKEN not configured in environment")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for chat_id in CHAT_IDS:
        payload = {
            "chat_id": chat_id,
            "text": text
        }
        try:
            response = requests.post(url, data=payload, timeout=10)
        except Exception as e:
            print(f"Failed to send to {chat_id}: {e}")
            continue

        if response.status_code != 200:
            print(f"Failed to send to {chat_id}: {response.status_code} {response.text}")


if __name__ == "__main__":
    hadith_text = get_random_hadith()
    send_telegram_message(hadith_text)