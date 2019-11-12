import vk_api, time, random

vk = vk_api.VkApi(token="c4cf0a0ac196623b06a0799377938038521e702a702134cf7f75d8ddd62f4e25f48c5c1b19109e1c8a4c7" )

print("VK bot is active")

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})

    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        text = messages["items"][0]["last_message"]["text"]


        if text.lower() == "привет":
            vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 999999)})
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Я не понял тебя","random_id": random.randint(1, 999999)})

        time.sleep(1)
        

