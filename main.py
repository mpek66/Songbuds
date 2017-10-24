import init

#addusers
while True:
    newuserin = input("Enter a New User or Type 'Done': ")
    if newuserin == 'Done' and len(users)>=2:
        break
    elif newuserin == 'Done' and len(users) <2:
	print("You Need at Least Two Users")
    elif not newuserin in users:
	users.append({'name': newuserin, 'songs': {}, 'subshared': []})

def main():
    #master user
    users = []
    masteruser = input("Enter the Master User: ") #master user is the user with the token
    users.append({'name': masteruser, 'songs': {}, 'subshared': []})
    sp = init.generate_user(masteruser)
    #common songs
    sharedsongs = []
    sharedids = []

def remove_duplicate_songs(songs):
    result = {}
    for key in songs:
        if key not in result.keys():
            result[key] = songs[key]
    return result

def remove_deplicates(songs):
    result = []
    for song in songs:
        if song not in result:
            result.append(song)
    return result

def binary_search_song(song,songdict):
    songlist = list(songdict.keys())
    songlist.sort()
    ub = len(songlist)-1
    lb = 0
    for x in range(100):
        index = (ub+lb)//2
        if songlist[index] == song:
            return True
        if songlist[index]>song:
            ub = index
        else:
            lb = index

def count_num(song, songlist):
    result = 0
    for s in songlist:
        if song == s:
            result += 1
    return result

def rank_off_occurances(songs):
    songs.sort()
    result = []
    most_occurances = 0
    for song in songs:
        num = count_num(song,songs)
        if num>most_occurances:
            most_occurances = num
    level = most_occurances
    while level>0:
        for song in songs:
            if count_num(song,songs) == level:
                result.append(song)
        level -= 1
    result = remove_deplicates(result)
    return result

percent_tracker = 0 #thing to track percent completeion

#each user, initialize a dictionary of unique songs
for user in users:
    percent_tracker += 1
    all_playlists = sp.user_playlists(user['name']) #list of playlists
    for playlist in all_playlists['items']: #each playlist
        if playlist['owner']['uri'].split(':')[2] == user['name']: #if our user is the owner
            tracks = sp.user_playlist_tracks(user['name'],playlist['id'] ) #broad tracks
            for item in tracks['items']: #for each broad track
                user['songs'][item['track']['name']] = item['track']['id']
    user['songs'] = remove_duplicate_songs(user['songs'])
    print(str(percent_tracker*50//len(users)) + "%")

total_searches = len(users)*(len(users)-1)/2
percent_tracker = 0 #variables used to update percent completeion

for index1 in range(len(users)):
	#create list of common songs
    for index2 in range(index1+1,len(users)):
        percent_tracker+=1
        if len(users[index1]['songs'].keys()) >0 and len(users[index2]['songs'].keys())>0:
            for song in users[index1]['songs']:
                if binary_search_song(song,users[index2]['songs']):
                    sharedsongs.append(song)
                    sharedids.append(users[index1]['songs'][song])
            print(str(int(50 + (percent_tracker*50)//total_searches)) + "%")

sharedsongs = rank_off_occurances(sharedsongs)
sharedids = rank_off_occurances(sharedids)

max_length = int(input("Enter a Maximum Number of Songs: "))
if max_length > 99:
    max_length = 99

while len(sharedsongs)>=max_length:
    sharedsongs.pop()
    sharedids.pop()

#create playlist
playname = input("Enter a Name for the Playlist: ")
playlist = sp.user_playlist_create(users[0]['name'], playname)
sp.user_playlist_add_tracks(users[0]['name'],playlist['id'], sharedids)

print("Success! Playlist Created")
