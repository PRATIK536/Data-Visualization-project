import requests

BOT_TOKEN = '8332131170:AAHdXdwMDViYtlfFnFjTmwtD_zFTFCjRI5w'
CHAT_ID = 'Avalue2_bo'
MESSAGE = 'Hello from your Python bot'

def send_message():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': MESSAGE
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(" Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

send_message()
