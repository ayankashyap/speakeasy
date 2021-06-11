import requests

dictToSend = {'input': 'Triple X'}  # change the input text here
res = requests.post('http://localhost:5000/convert', json=dictToSend)
print('response from server:', res.text)
