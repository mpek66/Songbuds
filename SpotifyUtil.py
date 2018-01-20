from Spotipy.spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import json

def generate_master_user(username):
    #initialization and authentication
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,scope,"56937ed556914553aa22ecedb2fbcc74","d589c26ddb5d4365862fa0056c3431f8","http://localhost:8888")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        return sp
    else:
        return None

#takes a username, and a spotify object and a list of sorted unique track ids
def generate_songs(user, sp):
    result = []
    all_playlists = sp.user_playlists(user) #list of playlists
    for playlist in all_playlists['items']: #each playlist
        if playlist['owner']['uri'].split(':')[2] == user: #if our user is the owner
            tracks = sp.user_playlist_tracks(user,playlist['id'] ) #broad tracks
            for item in tracks['items']: #for each broad track
                track_id  = item['track']['id']
                if track_id != None:
                    if len(result) == 0:
                        result.append(track_id)
                    else:
                        ix = 0
                        while ix < len(result) and track_id > result[ix]:
                            #loop to find correct index to insert
                            ix += 1
                        if ix == len(result):
                            #if correct position is end of list
                            result.append(track_id)
                        elif track_id != result[ix]:
                            #if the list does not already contain this id
                            result.insert(ix, track_id)
    return result

#creates a playlist under the given user
#requres a list of song ids, a name, and a spotipy object with a token for the given user
def create_playlist(playlistname, songids, username, sp):
    playlist = sp.user_playlist_create(username, playlistname)
    sp.user_playlist_add_tracks(username, playlist['id'], songids[:100])

#a function to get a song name given its id
def get_song_name(song_id, sp):
    track= sp.track(song_id)
    return track['name']
