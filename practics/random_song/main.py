import requests
from threading import Thread
import queue
import pprint




ACCES_TOKEN = 'lHyRkci_m7xiVuFyYyaxsBhYg6SnWIq-2REsiTV_P3iGFpDl-oYCpwTOggLbFhNO'
GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'
HEADERS = {
    'Accept': 'application/json',
    'Authorization': f'Bearer t8QrEqKX0LDgkP3ZXWIWeFaKIUUPnEA80f4aUzP0NfMTtV7sR_MUlOXgPp85BCG6'
    }

#https://genius.com/songs/10826052/apple_music_player?react=1


class Genre(Thread):
    def __init__(self, query):
        super().__init__()
        self.query = query

    def run(self):
        genre = requests.get(GENRE_API_URL).json()
        self.query.put(genre)



class Genius(Thread):
    def __init__(self, query):
        super().__init__()
        self.query = query

    def run(self):
        genre = self.query.get()
        data = requests.get(GENIUS_API_URL, headers=HEADERS, params={'acces_token': ACCES_TOKEN, 'q': genre})
        data = data.json()
        song_id = data['response']['hits'][0]['result']['api_path']
        pprint.pprint(data['response']['hits'][0])
        print(f'{GENIUS_URL}{song_id}/apple_music_player')


query = queue.Queue(maxsize=1)
genre = Genre(query)
song = Genius(query)
genre.start()
song.start()
genre.join()
song.join()