import json
import requests

url = 'http://127.0.0.1:8000/fresherbell_quiz_api'

input_data_for_model = {
    'id': 2
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data = input_json)
for i in response:
    print(i)