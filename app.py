from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.app import App
from kivy.lang import Builder
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

<MenuScreen>:
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size
    Label:
        font_size: 70
        text: 'Welcome to Celebrities!'
    Button:
        text: 'Play'
        size_hint: None, None
        pos: root.width/4, root.top * 0.25 + 100
        size: 200, 100
        on_release: root.manager.current = root.manager.next()
    Button:
        text: 'About'
        size_hint: None, None
        size: 200, 100
        pos: root.width * 0.75 - 200, root.top * 0.25 + 100
        on_release: root.manager.current = 'about'
    Button:
        text: 'Settings'
        size_hint: None, None
        size: 200, 100
        pos: root.width/4, root.top * 0.125 + 100
        on_release: root.manager.current = 'settings'
    Button:
        text: 'Rules'
        size_hint: None, None
        size: 200, 100
        pos: root.width * 0.75 - 200, root.top * 0.125 + 100
        on_release: root.manager.current = 'rules'

<SettingsScreen>:
    canvas:
        Color:
            hsv: self.hue, .8, .2
        Rectangle:
            size: self.size
    Label:
        font_size: 70
        text: 'Settings'
    Button:
        text: 'No. of players'
        size_hint: None, None
        pos: root.width/4, root.top * 0.25 + 100
        size: 250, 100
        on_release: root.manager.current = root.manager.next()
    Button:
        text: 'Cards per player'
        size_hint: None, None
        size: 250, 100
        pos: root.width * 0.75 - 200, root.top * 0.25 + 100
        on_release: root.manager.current = root.manager.previous()
    Button:
        text: 'No. of rounds'
        size_hint: None, None
        size: 250, 100
        pos: root.width/4, root.top * 0.125 + 100
        on_release: root.manager.current = root.manager.previous()
    Button:
        text: 'Round timer'
        size_hint: None, None
        size: 250, 100
        pos: root.width * 0.75 - 200, root.top * 0.125 + 100
        on_release: root.manager.current = root.manager.previous()
    Button:
        text: 'Main Menu'
        size_hint: None, None
        size: 250, 100
        pos_hint: {'right': 1}
        on_release: root.manager.current = 'menu'

<AboutScreen>:
    canvas:
        Color:
            hsv: self.hue, .8, .2
        Rectangle:
            size: self.size
    Label:
        font_size: 70
        text: 'About'

    Button:
        text: 'Main Menu'
        size_hint: None, None
        size: 250, 100
        pos_hint: {'right': 1}
        on_release: root.manager.current = 'menu'

<RulesScreen>:
    canvas:
        Color:
            hsv: self.hue, .8, .2
        Rectangle:
            size: self.size
    Label:
        font_size: 70
        text: 'Rules'

    Button:
        text: 'Main Menu'
        size_hint: None, None
        size: 250, 100
        pos_hint: {'right': 1}
        on_release: root.manager.current = 'menu'
''')

class MenuScreen(Screen):
    hue = NumericProperty(0)

class SettingsScreen(Screen):
    hue = NumericProperty(1)

class AboutScreen(Screen):
    hue = NumericProperty(2)

class RulesScreen(Screen):
    hue = NumericProperty(3)

class DurationClock(Label):
    def update(self, index, *args):
        self.text = index

class Celebrities(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(MenuScreen(name= 'menu'))
        root.add_widget(SettingsScreen(name= 'settings'))
        root.add_widget(AboutScreen(name= 'about'))
        root.add_widget(RulesScreen(name= 'rules'))
        return root

if __name__ == '__main__':
    Celebrities().run()
