import requests

BOT_TOKEN = '6054063200:AAHMJ_JnDLBJSfppwQswOTW-kHzBQY6xbZk'
URL = f'https://api.telegram.org/bot6054063200:AAHMJ_JnDLBJSfppwQswOTW-kHzBQY6xbZk/sendMessage'

response = requests.post(URL, data={'chat_id': '@fudiot_bot', 'text': 'Hello, World!'})
chat_id = response.json()['result']['chat']['id']
print(chat_id)
