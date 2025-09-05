import requests

BOT_TOKEN = '8332131170:AAHdXdwMDViYtlfFnFjTmwtD_zFTFCjRI5w'
telegram_group_id = "Avalue2_bo"

def get_chat_id():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
    response = requests.get(url)
    data = response.json()

    for result in data['result']:
        if 'message' in result:
            chat = result['message']['chat']
            print(f"Group Name: {chat.get('title', 'N/A')}")
            print(f"Chat ID: {chat['Avalue2_bo']}")
            break

get_chat_id()