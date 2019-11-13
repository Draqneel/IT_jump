import requests, vk_api, datetime, random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

vk_session = vk_api.VkApi(token='c4cf0a0ac196623b06a0799377938038521e702a702134cf7f75d8ddd62f4e25f48c5c1b19109e1c8a4c7')
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)
session = requests.Session()
attachments = []

data = {
    'dog': 'https://www.washingtonpost.com/resizer/6VLkVDjp4HgJILu4rzHNeLQugLc=/1440x0/smart/arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/HB4AT3D3IMI6TMPTWIZ74WAR54.jpg',
    'cat': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.c-ville.com%2Fcat-pause-if-your-pet-has-a-terminal-virus-dont-panic%2F&psig=AOvVaw29pZ8KogXTfRgx-TaSZQoi&ust=1573772370765000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDEnPuk6OUCFQAAAAAdAAAAABAD'
}

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
        if event.text.lower() == "время":
            d = datetime.datetime.today()

            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = random.randint(1,999999),
                    message = 'Текущее время: {}:{}:{}, {}.{}.{}'.format(d.hour, d.minute, d.second, d.day, d.month, d.year)  
                )

            elif event.from_chat:
                vk.messages.send(
                    user_id = event.chat_id,
                    random_id = random.randint(1,999999),
                    message = 'Текущее время: {}:{}:{}, {}.{}.{}'.format(d.hour, d.minute, d.second, d.day, d.month, d.year)
                )
        
        if event.text.lower() == "собака":
            
            image = session.get(data['dog'], stream= True)
            photo = upload.photo_messages(photos=image.raw)[0]

            attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))

            vk.messages.send(
                    user_id = event.user_id,
                    random_id = random.randint(1,999999),
                    attachment = ','.join(attachments),
                    message = 'Это пёсель'
                )

        