import json
from flask import Flask, Blueprint, request, redirect, g, render_template, Session, url_for, jsonify
import requests
from authentication import session, CLIENT_ID, CLIENT_SECRET, SPOTIFY_API_URL, \
    SPOTIFY_TOKEN_URL, SPOTIFY_API_BASE_URL, API_VERSION, SPOTIFY_API_URL
from extensions import db

creator = Blueprint('creator', __name__)

"""
takes data of the form:
algorithm: String,
group: List,
options: Object,
    depends on algorithm
playlistInfo: Object
    name: String,
    desc: String,
    maxSongs: Number,
"""
@creator.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    data = request.get_json()
    print(data)
    algorithm = data["algorithm"]
    songs = []
    status = "SUCCESS"
    if algorithm == "basic":
        group = data["group"]
        songs = basic_get_songs(group, data["options"])
    playlistInfo = data["playlistInfo"]
    create_playlist(songs, playlistInfo)
    return jsonify(status=status, data=songs[:playlistInfo["maxSongs"]])

@creator.route("/test", methods=["GET"])
def test():
    userid = session["profile_data"]["id"]
    songs = load_common_songs([userid,userid])
    playlistInfo = {
        "name": "name",
        "description": "description",
        "maxSongs": 50
    }
    create_playlist(songs, playlistInfo)
    return jsonify(done="done")

def create_playlist(songs, playlistInfo):
    userid = session["profile_data"]["id"]
    playlist_api_endpoint = "{}/v1/users/{}/playlists".format(SPOTIFY_API_BASE_URL,userid)
    headers = {
        "Authorization": session["authorization_header"]["Authorization"],
        "Content-Type": "application/json",
    }
    data = {
        "name": playlistInfo["name"],
        "public": True,
        "description": playlistInfo["description"],
    }
    playlists_response = requests.post(playlist_api_endpoint, headers=headers, data=json.dumps(data))
    playlist_id = playlists_response.json()["id"]
    add_track_api_endpoint = "{}/v1/playlists/{}/tracks".format(SPOTIFY_API_BASE_URL,playlist_id)
    uris = []
    ix = 0
    while len(uris) < playlistInfo["maxSongs"] and ix < len(songs):
        uris.append(songs[ix]["uri"])
        ix += 1
    data = {
        "uris": uris
    }
    add_track_response = requests.post(add_track_api_endpoint, headers=headers, data=json.dumps(data))

def load_user_songs(userid):
    playlist_api_endpoint = "{}/v1/users/{}/playlists".format(SPOTIFY_API_BASE_URL,userid)
    playlists_response = requests.get(playlist_api_endpoint, headers=session["authorization_header"])
    playlist_data = json.loads(playlists_response.text)
    songs = []
    for playlist in playlist_data["items"]:
        tracks_api_endpoint = "{}/playlists/{}/tracks".format(SPOTIFY_API_URL, playlist["id"])
        tracks_response = requests.get(tracks_api_endpoint, headers=session["authorization_header"])
        track_data = json.loads(tracks_response.text)
        for track in track_data["items"]:
            song = {
                "uri": track["track"]["uri"],
                "name": track["track"]["name"]
            }
            songs.append(song)
    return songs

#basically the same as load_common_songs, with importance modifiers, maybe better practice
def basic_get_songs(users, scale):
    uris = {}
    toname = {}
    for user in users:
        songs = load_user_songs(user)
        for song in songs:
            uris[song["uri"]] = uris.get(song["uri"],0.0) + float(scale[user])
            toname[song["uri"]] = song["name"]
    uris = sorted(uris, key=uris.get, reverse=True)
    songs = []
    for uri in uris:
        song = {
            "uri": uri,
            "name": toname[uri]
        }
        songs.append(song)
    return songs

def load_common_songs(users):
    uris = {}
    toname = {}
    for user in users:
        songs = load_user_songs(user)
        for song in songs:
            uris[song["uri"]] = uris.get(song["uri"],0) + 1
            toname[song["uri"]] = song["name"]
    uris = sorted(uris, key=uris.get, reverse=True)
    songs = []
    for uri in uris:
        song = {
            "uri": uri,
            "name": toname[uri]
        }
        songs.append(song)
    return songs
