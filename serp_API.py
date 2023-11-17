from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
import requests
load_dotenv()

# params = {
#     "engine": "google_maps",
#     "q": "Granite Restaurant",
#     "ll": "@40.7455096,-74.0083012,15.1z",
#     "type": "search",
#     "api_key": os.getenv("SERP_API_KEY")
# }

# from serpapi import GoogleSearch

params = {
    "engine": "google_maps",
    "type": "place",
    "data": "!4m5!3m4!1s0x89e26a96e0ab62ad:0x910e3b39e8d7b9f9!8m2!3d43.2011568!4d-71.54422389999999",
    "api_key": os.getenv("SERP_API_KEY")
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
# place_results.booking_link = results["place_results.booking_link"]


# print(os.getenv("SERP_API_KEY"))
# search = GoogleSearch(params)
# results = search.get_dict()
# print(results)
# place_result = results.get('place_results')
# if place_result:
#     # Get the first place from the search results
#     first_place = place_result
#     # print(first_place)
#     if 'gps_coordinates' in first_place:
#         lat = first_place['gps_coordinates']['latitude']
#         lng = first_place['gps_coordinates']['longitude']
#         # Generate the URL for the static map image
#         map_image_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=14&size=400x400&key=YOUR_STATIC_MAPS_API_KEY"
#         print(map_image_url)
#     else:
#         print("No GPS coordinates found for this place.")
# else:
#     print("No place results found.")
# local_results = results["local_results"]
# print(local_results)
