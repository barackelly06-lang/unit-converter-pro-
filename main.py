from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.spinner import Spinner 
from kivy.uix.label import Label

class ConverterApp(App): 
    def build(self): 
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10) 
        self.input = TextInput(hint_text='Weka namba hapa', multiline=False, font_size=32, input_filter='float') 
        layout.add_widget(self.input) 
        
        self.spinner_from = Spinner(text='Meters', values=('Meters', 'Kilometers', 'Grams', 'Kilograms')) 
        self.spinner_to = Spinner(text='Kilometers', values=('Meters', 'Kilometers', 'Grams', 'Kilograms')) 
        
        layout.add_widget(self.spinner_from) 
        layout.add_widget(self.spinner_to) 
        
        btn = Button
