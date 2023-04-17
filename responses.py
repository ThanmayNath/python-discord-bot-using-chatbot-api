import random
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    
    url = os.environ.get('URL')

    querystring = {"message":p_message,"uid":os.environ.get('UID')}

    headers = {
	os.environ.get('API-KEY'): os.environ.get('KEY'),
	os.environ.get('API-HOST'): os.environ.get('HOST')
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_dict = json.loads(response.text)
    print(response_dict['chatbot']['response'])

    return (response_dict['chatbot']['response'])
