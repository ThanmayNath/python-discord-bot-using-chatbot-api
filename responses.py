import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_response(message: str) -> str:
    p_message = message.lower()
    prompt=os.environ.get('DETAIL')+message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    url = os.environ.get('URL')
    payload = {
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": os.environ.get('UID'),
			"content": prompt
		}
	]
    }
    headers = {
	"content-type": "application/json",
	os.environ.get('API-KEY'):os.environ.get('KEY'),
	os.environ.get('API-HOST'):os.environ.get('HOST')
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    response_dict = json.loads(response.text)
    content = response_dict["choices"][0]["message"]["content"]
    print(content)
    return content