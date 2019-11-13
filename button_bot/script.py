import vk_api, json, random, time

vk = vk_api.VkApi(token="c4cf0a0ac196623b06a0799377938038521e702a702134cf7f75d8ddd62f4e25f48c5c1b19109e1c8a4c7")

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [
        [
        get_button(label="Кнопка1", color="positive"),
        get_button(label="Кнопка2", color="negative"),
        get_button(label="Кнопка3", color="primary"),
        get_button(label="Кнопка4", color="default"),
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def get_data(word):
    if (word == "Father"):
        data = {}
        #
        #
        #
        return data
    return None

def data_processing_father(data):
    pass


while (True):
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})

    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        text = messages["items"][0]["last_message"]["text"]


        if text.lower() == "привет":
            vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 999999)})
        elif text == "клавиатура":
            vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 999999), "keyboard": keyboard})
        elif text == "Кнопка1":
            vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 999999)})
        elif text == "Кнопка2":
            vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 999999)})
        elif text == "Кнопка3":
            vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 999999)})
        elif text == "Кнопка4":
            vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 999999)})
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Я не понял тебя","random_id": random.randint(1, 999999)})

        time.sleep(1)

