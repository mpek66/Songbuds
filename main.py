import Algorithms
import UserUtil
import AppObjects
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(Screen):
    pass

class VerificationScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class CreateScreen(Screen):
    pass

class FriendsScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class SongBudsApp(App):
    #details to be loaded about the user
    master = StringProperty("")
    level = NumericProperty(0)
    songs_generated = NumericProperty(0)
    #the userlist
    UL = ObjectProperty(UserUtil.UserList())
    
    def build(self):
        return Manager()

    #a function to try to login
    def login(self, username, remember):
        self.UL = UserUtil.UserList()
        self.UL.create_master(username)
        self.master = username
        self.root.current = 'home'

    def create_playlist(self, users, playname):
        self.UL.set_users(users)
        songs = Algorithms.algorithm_v1(self.UL)
        self.UL.create_playlist(playname, songs)

if __name__ == "__main__":
    Builder.load_file("objects.kv")
    Builder.load_file("screens.kv")
    Songbuds = SongBudsApp()
    Songbuds.run()
