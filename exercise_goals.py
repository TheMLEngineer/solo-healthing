from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ExerciseGoals(Screen):
    def __init__(self, **kwargs):
        super(ExerciseGoals, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.goal_label = Label(text='Exercise Goals')
        self.goal_button1 = Button(text='Goal 1')
        self.goal_button2 = Button(text='Goal 2')
        self.goal_button3 = Button(text='Goal 3')
        
        self.layout.add_widget(self.goal_label)
        self.layout.add_widget(self.goal_button1)
        self.layout.add_widget(self.goal_button2)
        self.layout.add_widget(self.goal_button3)
        self.add_widget(self.layout)
        
        self.goal_button1.bind(on_press=self.complete_goal)
        self.goal_button2.bind(on_press=self.complete_goal)
        self.goal_button3.bind(on_press=self.complete_goal)

    def complete_goal(self, instance):
        instance.text = 'Completed'
