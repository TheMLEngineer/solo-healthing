from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.clock import Clock

class WaterReminder(Screen):
    def __init__(self, **kwargs):
        super(WaterReminder, self).__init__(**kwargs)
        self.label = Label(text='Drink water reminder')
        self.add_widget(self.label)
        Clock.schedule_interval(self.reminder, 3600)  # Reminder every hour

    def reminder(self, dt):
        self.label.text = 'Time to drink water!'
