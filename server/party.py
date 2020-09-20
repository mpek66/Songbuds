import json
from flask import Flask, Blueprint, request, redirect, g, render_template, Session, url_for, jsonify
import requests
from authentication import session, CLIENT_ID, CLIENT_SECRET, SPOTIFY_API_URL, \
    SPOTIFY_TOKEN_URL, SPOTIFY_API_BASE_URL, API_VERSION, SPOTIFY_API_URL
from extensions import db
from models import Parties
from create import load_common_songs

partyer = Blueprint('partyer', __name__)

@partyer.route("/lookup_guest", methods=["GET"])
def lookup_guest():
    username = request.args["username"]
    status = "SUCCESS"
    user_api_endpoint = "{}/v1/users/{}".format(SPOTIFY_API_BASE_URL,username)
    headers = {
        "Authorization": session["authorization_header"]["Authorization"],
    }
    user_response = requests.get(user_api_endpoint, headers=headers)
    raw_data = json.loads(user_response.text)
    if raw_data.get("error",{}).get("status",None) == 404:
        return jsonify(status=status, data=None)
    print(raw_data)
    photo = None
    if len(raw_data["images"]) > 0:
        photo = raw_data["images"][0].get("url", None)
    href = None
    if len(raw_data["external_urls"]) > 0:
        href = raw_data["external_urls"].get("spotify", None)
    data = {
        "photo": photo,
        "username": username,
        "href": href,
    }
    return jsonify(status=status, data=data)

@partyer.route("/party_exists", methods=["GET"])
def party_exists():
    party = Parties.query.filter_by(user=session["profile_data"]["id"]).first()
    status = "SUCCESS"
    data = None
    if party is not None:
        data = {
            "user": party.user,
            "songs": party.songs,
            "users": party.users
        }
    print(db.session.query(Parties.user).all())
    return jsonify(status=status, data=data)

@partyer.route("/start_party", methods=["POST"])
def start_party():
    indata = Parties(session["profile_data"]["id"], [], [session["profile_data"]["id"]])
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print(e)
    return jsonify(status="SUCCESS")


@partyer.route("/add_guest", methods=["POST"])
def add_guest():
    guest = request.get_json()["user"]
    party = Parties.query.filter_by(user=session["profile_data"]["id"]).first()
    users = party.users[:]
    songs = party.songs[:]
    adding = {}
    toname = {}
    for user in users:
        common = load_common_songs([guest, user])
        for song in common:
            already = False
            for existsong in songs:
                if song["uri"] == existsong["uri"]:
                    already = True
                    break
            if not already:
                adding[song["uri"]] = adding.get(song["uri"],0) + 1
                toname[song["uri"]] = song["name"]
    adding = sorted(adding, key=adding.get, reverse=True)
    final = []
    for uri in adding[:5]:
        song = {
            "uri": uri,
            "name": toname[uri]
        }
        final.append(song)
    songs.extend(final)
    users.append(guest)
    party.songs = songs
    party.users = users
    db.session.commit()
    data = {
        "user": party.user,
        "users": users,
        "songs": songs
    }
    return jsonify(status="SUCCESS", data=data)

@partyer.route("/end_party", methods=["POST"])
def end_party():
    try:
        parties = Parties.query.filter_by(user=session["profile_data"]["id"]).all()
        for party in parties:
            db.session.delete(party)
            db.session.commit()
    except Exception as e:
        print(e)
    return jsonify(status="SUCCESS")
