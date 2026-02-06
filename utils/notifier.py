import requests
import os

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

def send_alert(message: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("[!] Telegram env not set")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        r = requests.post(url, json=payload, timeout=10)
        if r.status_code != 200:
            print("[!] Telegram error:", r.text)

    except Exception as e:
        print(f"[!] Telegram send failed: {e}")
