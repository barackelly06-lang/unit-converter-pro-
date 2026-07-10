from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner

class UnitConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='Unit Converter Pro', font_size=24)
        self.layout.add_widget(self.label)
        
        self.input = TextInput(text='1', multiline=False, font_size=20)
        self.layout.add_widget(self.input)
        
        self.spinner_from = Spinner(
            text='Meters',
            values=('Meters', 'Kilometers', 'Centimeters', 'Inches', 'Feet')
        )
        self.layout.add_widget(self.spinner_from)
        
        self.spinner_to = Spinner(
            text='Centimeters', 
            values=('Meters', 'Kilometers', 'Centimeters', 'Inches', 'Feet')
        )
        self.layout.add_widget(self