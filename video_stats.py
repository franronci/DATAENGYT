import os
import requests

CHANNEL_HANDLE = 'SantiagoMagnin'
API_KEY = os.getenv("YOUTUBE_API_KEY") or os.getenv("API_KEY")

def get_playlist_id():

    try:

        url=f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        channel_items = data["items"][0]

        channel_playlist = channel_items["contentDetails"]["relatedPlaylists"]['uploads']

        ##print(channel_playlist)

        return channel_playlist

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == '__main__':

    get_playlist_id()
