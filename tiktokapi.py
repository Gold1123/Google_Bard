import re
from TikTokApi import TikTokApi
import requests

def get_video_id_from_url(url):
    match = re.search(r'video/(\d+)', url)
    return match.group(1) if match else None

def download_video(video_bytes, name):
    with open(name + '.mp4', 'wb') as f:
        f.write(video_bytes)

def main(url):
    api = TikTokApi()
    video_id = get_video_id_from_url(url)
    tiktok = api.get_tiktok_by_id(video_id)
    video_bytes = requests.get(tiktok['itemInfo']['itemStruct']['video']['downloadAddr']).content
    download_video(video_bytes, video_id)

url = "https://www.tiktok.com/@troyesivan/video/7300529173037092127"
if __name__ == "__main__":
    main(url)