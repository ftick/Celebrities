from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
from kivy.lang import Builder
from functools import partial
from game import Deck, Team

# provides the kivy input for graphics
Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import SwapTransition kivy.uix.screenmanager.SwapTransition
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
#:import FallOutTransition kivy.uix.screenmanager.FallOutTransition
#:import NoTransition kivy.uix.screenmanager.NoTransition

<FillScreen>:
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size
    RelativeLayout:
        Label:
            font_size: 70
            text: 'Word'
            size: 400, 100
            pos_hint: {'x':1,'y':1}
        TextInput:
            multiline: False
            hint_text: 'Write your name here!'
            size_hint: None, None
            size: 150, 30
            pos_hint: {'center_x':0.5,'center_y':0.9}
        TextInput:
            multiline: False
            hint_text: 'Write your word here!'
            size_hint: None, None
            size: 200, 30
            pos_hint: {'center_x':0.5,'center_y':0.7}
        Button:
            text: 'Submit'
            size_hint: None, None
            pos_hint: {'right':0.9,'center_y':0.7}
            size: 80, 50
            on_release: root.manager.current = root.manager.next()
''')

class FillScreen(Screen):
    hue = NumericProperty(0)

class PlayerScreen(Screen):
    fue = NumericProperty(1)

class FillApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(FillScreen(name= 'fill'))
        return root

if __name__ == "__main__":
    FillApp().run()
