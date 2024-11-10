from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class AchievementTracker(Screen):
    def __init__(self, **kwargs):
        super(AchievementTracker, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.tracker_label = Label(text='Achievement Tracker')
        self.calendar = Label(text='Calendar here')

        self.layout.add_widget(self.tracker_label)
        self.layout.add_widget(self.calendar)
        self.add_widget(self.layout)
