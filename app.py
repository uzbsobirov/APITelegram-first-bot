import requests


API_url = 'https://api.telegram.org/bot5762026535:AAEBRfaTbYw-x8SFg2o1HvBXItJw5hZc2vk'

response = requests.get(url=API_url + '/getUpdates?offset=386230906').json()

print(response)

message = response['result'][0]['message']

chat_id = message['from']['id']
text = message['text']

send_message = requests.get(url=API_url + f'/sendMessage?chat_id={chat_id}&text=Hello got isi {text}')