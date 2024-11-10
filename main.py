from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from fast_timer import FastTimer
from water_reminder import WaterReminder
from exercise_goals import ExerciseGoals
from achievement_tracker import AchievementTracker

class SoloHealthingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FastTimer(name='fast_timer'))
        sm.add_widget(WaterReminder(name='water_reminder'))
        sm.add_widget(ExerciseGoals(name='exercise_goals'))
        sm.add_widget(AchievementTracker(name='achievement_tracker'))
        return sm

if __name__ == '__main__':
    SoloHealthingApp().run()
