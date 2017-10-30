import util

def get_users(alist):
    users = alist[:]
    #addusers
    while True:
        newuserin = input("Enter a New User or Type 'Done': ")
        if newuserin == 'Done' and len(users)>=2:
            break
        elif newuserin == 'Done' and len(users) <2:
            print("You Need at Least Two Users")
        elif not newuserin in users:
            users.append({'name': newuserin, 'songs': {}})
    return users

#takes a dictionary of songs
def remove_duplicates(songs):
    if type(songs) == dict: #if its a dictionary
        result = {}
        for key in songs:
            if key not in result.keys():
                result[key] = songs[key]
        return result
    else: #if its a list
        result = []
        for song in songs:
            if song not in result:
                result.append(song)
        return result

#takes a sorted list, return index if found or -1 if not
def binary_song_search(song, alist):
    #assumes list is sorted and no duplicates
    lb = 0
    ub = len(alist) - 1
    searching = True
    while searching:
        m = (lb + ub)//2
        if song == m: #found it
            return m
        elif song > m: #if midpoint too low
            lb = m + 1
        elif song < m: #if midpoint too high
            ub = m
        elif lb == ub: #if searching an empty list
            searching = False
    return -1 #if didn't find it, return -1

#binary search for list, trying to get rid of
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

#counts the number of songs in a songlist
def count_num(song, songlist):
    result = 0
    for s in songlist:
        if song == s:
            result += 1
    return result

#returns a new list as merge of two lists, unique items
def merge(a, b):
    #assumes lists are sorted, and no duplicates
    ai = 0
    bi = 0
    result = []
    going = True
    while going:
        if ai >= len(a):
            going = False
        elif bi >= len(b):
            going = False
        elif a[ai] == b[bi]:
            result.append(a[ai])
            ai += 1
            bi += 1
        elif a[ai] > b[bi]:
            bi += 1
        elif a[ai] < b[bi]:
            ai += 1
    return result

#takes a sorted list, returns a list of unique items in order of num occurences
def rank_off_occurances(songs):
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

def main():
    #master user
    users = []
    masteruser = input("Enter the Master User: ") #master user is the user with the token
    users.append({'name': masteruser, 'songs': {}})
    sp = util.generate_master_user(masteruser)
    #get other users
    users = get_users(users)
    print("Got Users")
    #get each users songs, as a unique dictionary
    ix = 0
    while ix < len(users):
        users[ix] = util.generate_songs(users[ix], sp)
    #generate list of common songs and ids
    print("Got Songs")
    sharedsongs = []
    sharedids = []
    fix = 0
    while fix < len(users):
        six = fix + 1
        while six < len(users[six:]):
            subsharedsongs = merge(users[fix]['songs'].keys().sort(), \
                              users[six]['songs'].keys().sort())
            subsharedids = merge(users[fix]['songs'].values().sort(), \
                              users[six]['songs'].values().sort())
            sharedsongs.extend(subsharedsongs)
            sharedids.extend(subsharedids)
            six += 1
        fix += 1
    print("Sorted songs")

    #create playlist
    playname = input("Enter a Name for the Playlist: ")
    playlist = sp.user_playlist_create(users[0]['name'], playname)
    sp.user_playlist_add_tracks(users[0]['name'],playlist['id'], sharedids)
    sharedsongs = rank_off_occurances(sharedsongs)
    sharedids = rank_off_occurances(sharedids)

    max_length = int(input("Enter a Maximum Number of Songs: "))
    if max_length > 99:
        max_length = 99

    while len(sharedsongs)>=max_length:
        sharedsongs.pop()
        sharedids.pop()
    print("Success! Playlist Created")

if __name__ == "__main__":
    main()
        
'''
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
'''
