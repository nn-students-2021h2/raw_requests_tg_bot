import requests
import json

TOKEN = '' # insert your token from BotFather here
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"
LONG_POLLING_TIMEOUT = 10

last_update_id = None
while True:
    r = requests.get(BASE_URL + 'getUpdates',
                     params={
                         'offset': last_update_id,
                         'timeout': LONG_POLLING_TIMEOUT
                     })
    response_dict = json.loads(r.text)
    print(r.status_code)
    print(r.text)
    for upd in response_dict["result"]:
        last_update_id = upd["update_id"] + 1
        msg = upd["message"]
        chat_id = msg["chat"]["id"]
        if "text" in msg:
            text = msg["text"]
            r = requests.post(BASE_URL + 'sendMessage', params={
                "chat_id": chat_id,
                "text": text.upper()
            })
