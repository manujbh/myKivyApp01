import kivy
import sqlite3
import string
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class MBApp(App):
    screen_names = ListProperty([])

    # this is a native function from Kivy to actually build the app using KV files
    def build(self):
        self.title = 'Guide'
        self.screen_names = sorted([
            'Buttons', 'ToggleButton', 'Sliders', 'ProgressBar', 'Switches',
            'CheckBoxes', 'TextInputs', 'Accordions', 'FileChoosers',
            'Carousel', 'Bubbles', 'CodeInput', 'DropDown', 'Spinner',
            'Scatter', 'Splitter', 'TabbedPanel + Layouts', 'RstDocument',
            'Popups', 'ScreenManager'])


if __name__ == '__main__':
    MBApp().run()