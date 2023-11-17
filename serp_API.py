from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import requests
load_dotenv()

params = {
    "engine": "google_maps",
    "q": "Granite Restaurant",
    "type": "search",
    "api_key": os.getenv("SERP_API_KEY")
}


search = GoogleSearch(params)
results = search.get_dict()

print(os.getenv("SERP_API_KEY"))
search = GoogleSearch(params)
results = search.get_dict()
place_result = results.get('place_results')
if not place_result:
    first_place = results.get('local_results')[0]
    # print(first_place)
    if 'gps_coordinates' in first_place:
        lat = first_place['gps_coordinates']['latitude']
        lng = first_place['gps_coordinates']['longitude']
        data_id = first_place['data_id']
        params = {
            "engine": "google_maps",
            "type": "place",
            "data": f"!4m5!3m4!1s{data_id}!8m2!3d{lat}!4d{lng}",
            "api_key": os.getenv("SERP_API_KEY")
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results['search_metadata']['google_maps_url']
    else:
        print("No GPS coordinates found for this place.")
else:
    print("No place results found.")
