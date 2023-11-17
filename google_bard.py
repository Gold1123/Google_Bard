import requests


def get_place_info(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "input": address,
        "inputtype": "textquery",
        "fields": "formatted_address,name,business_status,place_id",
        "key": api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = "AIzaSyBQwyJpdhd3olus7yHPQnIFiZilxnC8o5A"
address = "ADDRESS"
place_info = get_place_info(address, api_key)
if place_info is not None:
  print(place_info)
else:
  print("Failed to get a response from Google Places API")