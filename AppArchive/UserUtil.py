import SpotifyUtil

#a class to represent each user
class User:
    #contains a name, and a sorted list of unique track ids
    def __init__(self, username, sp):
        self.name = username
        self.songs = SpotifyUtil.generate_songs(username, sp)

#a class to represent a collection of users
#needs a master and a spotipy object
class UserList:
    #creates a userlist with empty eveything
    def __init__(self):
        self.sp = None
        self.master = ""
        self.users = []

    #a function to validate a master user
    #return 1 if all good
    #return 0 if can't get user
    #return -1 if network error
    def create_master(self, username):
        self.sp = SpotifyUtil.generate_master_user(username)
        self.master = username
        return 0

    def set_users(self, usernames):
        for person in usernames:
            self.users.append(User(person, self.sp))

    #creates a playlist given a list of song ids, and a name
    def create_playlist(self, name, songs):
        SpotifyUtil.create_playlist(name, songs, self.master, self.sp)
    
