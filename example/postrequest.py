import requests

dictToSend = {'input': 'Triple X'}
res = requests.post('http://localhost:5000/convert', json=dictToSend)
print('response from server:', res.text)
dictFromServer = res.json()
