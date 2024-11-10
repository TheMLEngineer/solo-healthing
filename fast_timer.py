from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class FastTimer(Screen):
    def __init__(self, **kwargs):
        super(FastTimer, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.timer_label = Label(text='Set Fasting Timer')
        self.start_button = Button(text='Start Timer')
        self.stop_button = Button(text='Stop Timer')
        
        self.layout.add_widget(self.timer_label)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.stop_button)
        self.add_widget(self.layout)

        self.start_button.bind(on_press=self.start_timer)
        self.stop_button.bind(on_press=self.stop_timer)

    def start_timer(self, instance):
        self.timer_label.text = 'Timer Started'

    def stop_timer(self, instance):
        self.timer_label.text = 'Timer Stopped'
