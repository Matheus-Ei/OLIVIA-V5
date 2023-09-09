# Import the Libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

# Import the modules
import system.messages as msg


# Settings of credentials
scope = "user-modify-playback-state user-read-playback-state"
client_id = "839e78754a4c487fb2e8d60cd2e8223d"
client_secret = "cab13022188848678f982ed37e5d40c4"
redirect_uri = "http://localhost:8080"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)) # Starts SpotifyOAuth
devices = sp.devices() # Check the connected devices


# Select song
def select(track_name):
    results = sp.search(q=track_name, type="track", limit=1) # Search for the song in spotify

    if results["tracks"]["items"]:
        track_uri = results["tracks"]["items"][0]["uri"] # Get the url of the song
        sp.start_playback(uris=[track_uri])
        return (f"Playing the selected music: {track_name}")
    else:
        msg.error("No music found with this name")


# Next song
def next():
    try:
        sp.next_track()
        return ("I skipped to the next song!")
    except spotipy.SpotifyException as e:
        msg.error("Error skipping to next song:", str(e))
        return ("Error skipping to next song:", str(e))


# Pause song
def pause():
    try:
        sp.pause_playback()
        return ("I paused the music!")
    except spotipy.SpotifyException as e:
        msg.error("Error pausing the song:", str(e))
        return ("Error pausing the song:", str(e))


# Play song
def play():
    try:
        sp.start_playback()
        return ("I'm playing the music!")
    except spotipy.SpotifyException as e:
        msg.error("Error playing the song:", str(e))
        return ("Error playing the song:", str(e))
