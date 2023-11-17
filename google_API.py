import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

cx = os.getenv("CX_ID")
api_key = os.getenv("GOOGLE_API_KEY")

keyword = "Author of 'A Tourist’s Guide to Love'"


def search(keyword, cx, api_key):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': keyword,
        'cx': cx,
        'key': api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    return data['items'][0]['link']


print(search(keyword, cx, api_key))


def get_image_url(search_term):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'q': search_term,
            'cx': cx,
            'key': api_key,
            'searchType': 'image',
            'num': 3
        }
        response = requests.get(url, params=params)
        response_json = json.loads(response.text)
        return response_json['items'][0]['link']
    except:
        print(response_json)
        return "https://www.lifespanpodcast.com/content/images/2022/01/Welcome-Message-Title-Card-2.jpg"


# print(get_image_url("Stolen Focus - Johann Hari"))
