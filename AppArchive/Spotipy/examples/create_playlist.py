# Creates a playlist for a user

import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util


if True:
    username = 'bobzoo00'
    playlist_name = 'hello'
else:
    print("Usage: %s username playlist-name" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, "playlist-modify-public", "56937ed556914553aa22ecedb2fbcc74","d589c26ddb5d4365862fa0056c3431f8","http://localhost:8888")

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)
