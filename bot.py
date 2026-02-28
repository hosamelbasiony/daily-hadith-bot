import os
import random
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# رابط JSON على GitHub (Raw file)
JSON_URL = "https://raw.githubusercontent.com/AhmedBaset/hadith-json/refs/heads/main/db/by_book/other_books/riyad_assalihin.json"

def get_random_hadith():
    response = requests.get(JSON_URL)

    print("STATUS:", response.status_code)
    print("HEADERS:", response.headers.get("content-type"))
    print("FIRST 300 CHARS:\n", response.text[:300])

    data = response.json()

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
