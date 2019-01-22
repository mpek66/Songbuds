from kivy.properties import StringProperty, ListProperty, BooleanProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.actionbar import ActionBar
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton

#a class to represent an input dialogue with short prompt
class LabeledInput(BoxLayout):
    prompt = StringProperty("")
    my_input = StringProperty("here")

#a class to represent a checkbox with short prompt
class LabeledCheck(BoxLayout):
    prompt = StringProperty("")
    my_input = BooleanProperty(False)

#the navigation bar at the top
class Navigation(BoxLayout):
    pass

#a class to represent a blank screen to make kivy easier
class BlankLayout(BoxLayout):
    pass

#a class to represent a label that fills itself on one line
class DynamicLabel(Image):
    text = StringProperty('')
    def on_text(self, *_):
        l = Label(text=self.text)
        l.font_size = '64'
        l.texture_update()
        self.texture = l.texture

#a class to represent the object the chooses the algorithm
class AlgorithmSelector(BoxLayout):
    pass

#an input box to get shit from user in an elegant way
class InputBox(Popup):
    data = ObjectProperty()
    def __init__(self, data, **kwargs):
        kwargs['auto_dismiss'] = False
        self.data = data
        super().__init__(**kwargs)
    def return_input(self, value):
        self.data.extend([value])
        self.dismiss()

#a class to represent a button to add, remove users
class UserItem(ListItemButton):
    pass

#a class to represent the object that adds, removes, selects users from the list
class UserManager(BoxLayout):
    users = ObjectProperty(None)
    user_list = ObjectProperty(None)
    def add_user(self):
        popup = InputBox(self.user_list.adapter.data)
        popup.title = "Enter a Username"
        popup.open()
    def remove_user(self):
        if self.user_list.adapter.selection:
            self.user_list.adapter.data.remove(\
                    self.user_list.adapter.selection[0].text)
        
