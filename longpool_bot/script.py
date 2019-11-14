import requests, vk_api, datetime, random

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload

vk_session = vk_api.VkApi(token='c4cf0a0ac196623b06a0799377938038521e702a702134cf7f75d8ddd62f4e25f48c5c1b19109e1c8a4c7')
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)
session = requests.Session()
# Keyboard settings
keyboard = VkKeyboard(one_time=True)
keyboard.add_button("cобака", VkKeyboardColor.POSITIVE)
keyboard.add_button("кот", VkKeyboardColor.NEGATIVE)
#
attachments = []

data = {
    'dog': 'https://www.washingtonpost.com/resizer/6VLkVDjp4HgJILu4rzHNeLQugLc=/1440x0/smart/arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/HB4AT3D3IMI6TMPTWIZ74WAR54.jpg',
    'cat': 'https://images.immediate.co.uk/production/volatile/sites/4/2018/08/iStock_000044061370_Medium-fa5f8aa.jpg?quality=45&crop=5px,17px,929px,400px&resize=960,413'
}

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
        if event.text.lower() == "время":
            d = datetime.datetime.today()

            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = random.randint(1,999999),
                    keyboard = keyboard.get_keyboard(),
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
            
            vk.messages.send(
                    user_id = event.user_id,
                    random_id = random.randint(1,999999),
                    attachment = 'photo{}_{}'.format(photo['owner_id'], photo['id']),
                    message = 'Это пёсель'
                )
        
        if event.text.lower() == "кот":
            
            image = session.get(data['cat'], stream= True)
            photo = upload.photo_messages(photos=image.raw)[0]
            
            vk.messages.send(
                    user_id = event.user_id,
                    random_id = random.randint(1,999999),
                    attachment = 'photo{}_{}'.format(photo['owner_id'], photo['id']),
                    message = 'Это котик'
                )


        