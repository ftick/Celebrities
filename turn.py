from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.lang import Builder
from functools import partial
import ConfigParser
from game import Deck, Team

time=0

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

<TurnScreen>:
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size
    RelativeLayout:
    Label:
        font_size: 50
        text: 'Round X'
        size: 400, 100
        pos_hint: {'right':1,'top':1.4}
    Label:
        font_size: 50
        text: 'XX:XX'
        size: 400, 100
        pos_hint: {'right':1,'top':1.3}
        name: 'Timer'
    Label:
        font_size: 70
        text: 'Word'
        size: 400, 100
        pos_hint: {'right':1,'top':1}
    Button:
        text: 'Discard'
        size_hint: None, None
        pos_hint: {'x':0,'y':0}
        size: 200, 100
        on_release: root.manager.current = root.manager.next()
    Button:
        text: 'Keep'
        size_hint: None, None
        pos_hint: {'right':1,'y':0}
        size: 200, 100
        on_release: root.manager.current = root.manager.next()
''')

class RoundClock(Label):
    def update(self, index, *args):
        self.text = index

class TurnScreen(Screen):
    hue = NumericProperty(0)
    clock = RoundClock(name='Timer')
    settings = ConfigParser.ConfigParser()
    settings.read('settings.ini')
    time = settings.get("Options", "timer_options")
    if time == '2 min':
        time = 120
    elif time == '1 min':
        time = 60
    else:
        time = 30
    for i in range(time, 0, -1):
        Clock.schedule_once(partial(clock.update, str(i)), time-i)

class TurnApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(TurnScreen(name= 'turn'))
        return root

if __name__ == "__main__":
    TurnApp().run()
