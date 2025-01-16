import requests

TOKEN = "8046570764:AAHmkOTv-5U8NHeUN0ms6msE-H05gX0gT7Y"
CHAT_ID = 5474985935

def send_location(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    keyboard = {
        "keyboard": [
            [{"text": "Joylashuv", "request_location": True}]
        ]
    }
    
    payload = {
        "chat_id": chat_id,
        "text": "Lokatsiya",
        "reply_markup": keyboard
    }
    
    response = requests.post(url, json=payload)
    return response.json()

send_location(CHAT_ID)


import requests
TOKEN = "8046570764:AAHmkOTv-5U8NHeUN0ms6msE-H05gX0gT7Y"
CHAT_ID = 5474985935

def send_contact(chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    keyboard = {
        "keyboard": [
            [{"text": "Contact", "request_location": True}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": True
    }
    
    payload = {
        "chat_id": chat_id,
        "text": "Location",
        "reply_markup": keyboard
    }
    
    requests.post(url, json=payload)

send_contact(CHAT_ID)