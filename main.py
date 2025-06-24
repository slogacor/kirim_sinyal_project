import requests

url = "https://sinyal-xauusd-jkt.fly.dev/xauusd-webhook"

payload = {
    "token": "your_token_here",
    "chat_id": "your_chat_id_here",
    "text": "📢 [TES] Bot XAUUSD aktif ✅ Siap kirim sinyal breakout otomatis!"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status:", response.status_code)
print("Respon:", response.text)
