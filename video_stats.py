import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

CHANNEL_HANDLE = 'SantiagoMagnin'
API_KEY =  os.getenv("API_KEY")
MAX_RESULTS = 50

def get_playlist_id():

    try:

        url=f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        channel_items = data["items"][0]

        channel_playlist = channel_items["contentDetails"]["relatedPlaylists"]['uploads']

        print(channel_playlist)

        return channel_playlist

    except requests.exceptions.RequestException as e:
        raise e

    




def get_video_id(playlistId):

    videos_ids = []

    pageToken = None

    base_url = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={MAX_RESULTS}&playlistId={playlist_id}&key={API_KEY}'

    try:
        
        while True:

            url = base_url

            if pageToken:
                url += f'&pageToken={pageToken}'

            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            for item in data.get('items',[]):

                video_id = item['contentDetails']['videoId']
                videos_ids.append(video_id)

            pageToken = data.get('nextPageToken')

            if not pageToken:
                break

        return videos_ids


    except requests.exceptions.RequestException as e:
        raise e 



if __name__ == '__main__':

    playlist_id = get_playlist_id()

    print(get_video_id(playlist_id))


