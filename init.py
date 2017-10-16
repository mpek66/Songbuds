from Spotipy.spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import json

def generate_user(username):
    #initialization and authentication
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,scope,"56937ed556914553aa22ecedb2fbcc74","d589c26ddb5d4365862fa0056c3431f8","http://localhost:8888/")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        return sp
    else:
        return none
