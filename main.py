from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        
        self.input = TextInput(hint_text='Weka namba hapa', font