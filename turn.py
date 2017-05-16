from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
import ConfigParser
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

<TurnScreen>:
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size
    Label:
        font_size: 70
        text: 'Word'
    Button:
        text: 'Play'
        size_hint: None, None
        pos: root.width/4, root.top * 0.25 + 100
        size: 200, 100
        on_release: root.manager.current = root.manager.next()
''')

class RoundClock(Label):
    def update(self, index, *args):
        self.text = index

class TurnApp(App):
    def build(self):
        clock = RoundClock()
        settings = ConfigParser.ConfigParser()
        settings.read('settings.ini')
        time = settings.get("example", "timer_options")
        if time == '2 min':
            time = 120
        elif time == '1 min':
            time = 60
        else:
            time = 30
        for i in range(time, 0, -1):
            Clock.schedule_once(partial(clock.update, str(i)), time-i)
        return clock

if __name__ == "__main__":
    TurnApp().run()
