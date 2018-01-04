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
    #assumes first username is the master
    def __init__(self, usernames):
        self.sp = SpotifyUtil.generate_master_user(usernames[0])
        self.users = []
        for person in usernames:
            self.users.append(User(person, self.sp))
            
    #returns the master user
    def master_user(self):
        return self.users[0]

    #creates a playlist given a list of song ids, and a name
    def create_playlist(self, name, songs):
        SpotifyUtil.create_playlist(name, songs, \
                    self.master_user().name, self.sp)
    
