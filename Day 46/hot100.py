from bs4 import BeautifulSoup
import requests
from secretstuff import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Ask User for special date to look up.
user_date = input("What date do you want to travel to? YYYY-MM-DD  ")

# Get song data from that date on Billboard Hot 100 using BeautifulSoup, and create a list of song titles.
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date}")
hot_100 = response.text

soup = BeautifulSoup(hot_100, "html.parser")
song_data = soup.find_all(class_="chart-element__information__song")
songs = [song.getText().strip('\n                        ') for song in song_data]

# Generate Spotify API auth, or other just create an instance of SpotiPy.
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path="token.txt"))
user_id = sp.current_user()["id"]

# Search Spotify for the songs in the list, then collect their Spotify URIs into a new list if available.

song_id_list = []
year = user_date.split("-")[0]
for song in songs:
    song_id = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        song_id_list.append(song_id['tracks']['items'][0]["uri"])
    except IndexError:
            pass

# Create a new playlist, and add the songs from the song list.

new_playlist_id = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False, description=f"Billboard's top songs from {user_date}")

sp.playlist_add_items(playlist_id=new_playlist_id["id"],items=song_id_list)







