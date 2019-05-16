import json
from flask import Flask, Blueprint, request, redirect, g, render_template, Session, url_for, jsonify
import requests
import base64
import urllib

authenticator = Blueprint('authentication', __name__)
session = Session()

# Authentication Steps, paramaters, and responses are defined at https://developer.spotify.com/web-api/authorization-guide/
# Visit this url to see all the steps, parameters, and expected response.

#  Client Keys
CLIENT_ID = "56937ed556914553aa22ecedb2fbcc74"
CLIENT_SECRET = "d589c26ddb5d4365862fa0056c3431f8"

# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)


# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 5000
REDIRECT_URI = "{}:{}/callback/q".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()


auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

@authenticator.route("/session")
def get_session():
    if "profile_data" in session:
        return jsonify(data=session["profile_data"])
    else:
        return jsonify(data=False)

@authenticator.route("/authorize")
def index():
    # Auth Step 1: Authorization
    url_args = ""
    for (key, val) in auth_query_parameters.items():
        url_args += "{}={}".format(key, urllib.parse.quote(val)) + "&"
    url_args = url_args[:-1]
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)

@authenticator.route("/callback/q")
def callback():
    # Auth Step 4: Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth Step 5: Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]
    session["access_token"] = access_token
    session["refresh_token"] = refresh_token
    session["token_type"] = token_type
    session["expires_in"] = expires_in

    # Auth Step 6: Use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}
    session["authorization_header"] = authorization_header

    # Get profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)
    session["profile_data"] = profile_data

    # Get user playlist data
    #playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    #playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    #playlist_data = json.loads(playlists_response.text)
    return redirect("http://localhost:8080/load")

@authenticator.route("/get_playlists")
def get_playlists():
    playlist_api_endpoint = "{}/playlists".format(session["profile_data"]["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=session["authorization_header"])
    playlist_data = json.loads(playlists_response.text)
    return jsonify(playlist_data)

@authenticator.route("/get_all_songs")
def get_all_songs():
    playlist_api_endpoint = "{}/playlists".format(session["profile_data"]["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=session["authorization_header"])
    playlist_data = json.loads(playlists_response.text)
    songs = []
    for playlist in playlist_data["items"]:
        tracks_api_endpoint = "{}/playlists/{}/tracks".format(SPOTIFY_API_URL, playlist["id"])
        tracks_response = requests.get(tracks_api_endpoint, headers=session["authorization_header"])
        track_data = json.loads(tracks_response.text)
        for track in track_data["items"]:
            songs.append(track["track"]["name"])
    return jsonify(songs)

@authenticator.route("/get_user_songs")
def get_user_songs():
    userid = request.args.get("username")
    return jsonify(load_user_songs(userid))

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
@authenticator.route("/generate_playlist", methods=["POST"])
def generate_playlist():
    data = request.get_json()
    algorithm = data["algorithm"]
    songs = []
    status = "SUCCESS"
    if algorithm != "basic":
        group = data["group"]
        songs = load_common_songs(group)
    playlistInfo = data["playlistInfo"]
    create_playlist(songs, playlistInfo)
    return jsonify({"status": status, "data": songs})

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
            songs.append(track["track"]["name"])
    return songs

def load_common_songs(users):
    allsongs = []
    finalsongs = []
    for user in users:
        songs = load_user_songs(user)
        for song in songs:
            if song not in allsongs:
                allsongs.append(song)
            elif song not in finalsongs:
                finalsongs.append(song)
    return finalsongs
