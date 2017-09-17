from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import json

#master user
users = []
masteruser = input("Enter the Master User: ") #master user is the user with the token
users.append({'name': masteruser, 'songs': {}, 'subshared': []})

#initialization and authentication
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(users[0]['name'],scope,"56937ed556914553aa22ecedb2fbcc74","d589c26ddb5d4365862fa0056c3431f8","http://localhost:8888/")
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
else:
	print("can't get token")

#addusers
while True:
	newuserin = input("Enter a New User or Type 'Done': ")
	if newuserin == 'Done' and len(users)>=2:
		break
	elif newuserin == 'Done' and len(users) <2:
		print("You Need at Least Two Users")
	elif not newuserin in users:
		users.append({'name': newuserin, 'songs': {}, 'subshared': []})

#common songs
sharedsongs = {}
#ordered ranking of how many times it appeared across users
rankedsongs = []
rankedid = []

for user in users: #each user
	all_playlists = sp.user_playlists(user['name']) #list of playlists
	for playlist in all_playlists['items']: #each playlist
		if playlist['owner']['uri'].split(':')[2] == user['name']: #if our user is the owner
			tracks = sp.user_playlist_tracks(user['name'],playlist['id'] ) #broad tracks
			for item in tracks['items']: #for each broad track
				user['songs'][item['track']['name']] = item['track']['id']
	#create list of common songs
	for user2 in users:
		if user != user2:
			for song in user['songs']:
				for song2 in user2['songs']:
					if user['songs'][song] == user2['songs'][song2] and song == song2: #songs equal?
						if not song in user['subshared']:
							user['subshared'].append(song)
							if song in sharedsongs.keys():
								sharedsongs[song][user['songs'][song]] += 1
							else:
								sharedsongs[song] = {user['songs'][song]: 1}
						if not song2 in user2['subshared']:
							user2['subshared'].append(song2)
							if song2 in sharedsongs.keys():
								sharedsongs[song][user2['songs'][song2]] += 1 
							else:
								sharedsongs[song] = {user2['songs'][song2]: 1}

#sort shared songs
highest = 0
while len(rankedsongs) != len(sharedsongs.keys()):
	for song in sharedsongs: #find highest count
		for key in sharedsongs[song]:
			if sharedsongs[song][key] > highest and not song in rankedsongs: #if highest
				highest = sharedsongs[song][key]
			if sharedsongs[song][key] == highest and song in rankedsongs: #if highest has already been added
				highest = 0
	for song in sharedsongs: #if highest count
		for key in sharedsongs[song]:
			if sharedsongs[song][key] == highest:
				rankedsongs.append(song)
				rankedid.append(key)

for songname in rankedsongs:
	for user in users:
		for song in user['songs']:
			if songname == song and not user['songs'][song] in rankedid:
				rankedid.append(user['songs'][song])
#double check no duplicates
for ii in range(0,len(rankedid)):
	for cc in range(0,len(rankedid)):
		if cc != ii and rankedid[ii] == rankedid[cc]:
			rangeid.pop[cc]

print(sharedsongs)

#create playlist
while len(rankedid)>100:
	rankedid.pop()
playname = input("Enter a Name for the Playlist: ")
playlist = sp.user_playlist_create(users[0]['name'], playname)
sp.user_playlist_add_tracks(users[0]['name'],playlist['id'], rankedid)

print("Success! Playlist Created")