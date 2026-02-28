import os
import random
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# رابط JSON على GitHub (Raw file)
JSON_URL = "https://raw.githubusercontent.com/USERNAME/REPO/main/hadith.json"

def get_random_hadith():
    response = requests.get(JSON_URL)
    data = response.json()

    # لو JSON عبارة عن Array مباشرة
    if isinstance(data, list):
        hadith = random.choice(data)
    else:
        # لو JSON فيه key زي "hadiths"
        hadith = random.choice(data["hadiths"])

    return hadith["text"] if "text" in hadith else str(hadith)

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
