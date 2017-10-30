from Spotipy.spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import json

def generate_master_user(username):
    #initialization and authentication
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,scope,"56937ed556914553aa22ecedb2fbcc74","d589c26ddb5d4365862fa0056c3431f8","http://localhost:8888/")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        return sp
    else:
        return none

#takes a user, and a spotify object and returns unique songs
def generate_songs(auser, sp):
    user = auser.copy()
    all_playlists = sp.user_playlists(user['name']) #list of playlists
    for playlist in all_playlists['items']: #each playlist
        if playlist['owner']['uri'].split(':')[2] == user['name']: #if our user is the owner
            tracks = sp.user_playlist_tracks(user['name'],playlist['id'] ) #broad tracks
            for item in tracks['items']: #for each broad track
                if item['track']['name'] not in user['songs']:
                    user['songs'][item['track']['name']] = item['track']['id']
    return user
