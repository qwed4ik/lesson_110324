import pprint
import requests
api = '6994860528:AAFT6Lbbm0Rqftmp-ME6XuG3EG0oCwwppc0'
main_url = f'https://api.telegram.org/bot{api}'
url = f'{main_url}/getMe'

result = requests.get(url)
print(result.json())

#Проверка на обновления
url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

#Ответ на сообщение
messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Саламалейкума!'
    }
    result = requests.post(url,params=params)