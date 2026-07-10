 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class UnitConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        self.add_widget(Label(text='Unit Converter Pro', font_size=24, size_hint_y=0.2))
        
        self.input = TextInput(text='1', multiline=False, font_size=20, size_hint_y=0.15)
        self.add_widget(self.input)
        
        self.spinner = Spinner(
            text='Meters