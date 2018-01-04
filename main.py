from Algorithms import *
from UserUtil import *
import kivy

#a funtion that gets usernames, returning a list of strings
def get_users():
    return ['ibelli16', 'bobzoo00']

#a function that gets the playlist name
def get_playlist_name():
    return input("Enter a name for the playlist: ")

def main():
    UL = UserList(get_users())
    songs = algorithm_v1(UL)
    UL.create_playlist(get_playlist_name(), songs)

if __name__ == "__main__":
    main()
