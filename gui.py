from kivy import platform
from kivy.uix.boxlayout import BoxLayout

if platform == 'win':
    from kivy.config import Config
    Config.set('graphics', 'resizable', False)
    Config.set('graphics', 'width', '500')
    Config.set('graphics', 'height', '1000')

from kivy.properties import StringProperty, NumericProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout


class AchieveTheGoalApp(MDApp):

    def __init__(self):
        super().__init__()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return MainScreen()


class MainScreen(MDBoxLayout):
    pass


class Heatmap(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.load_heatmap()

    def load_heatmap(self):
        level = {'level_0': [
            {'level_1a': [{'level_2a': []}, {'level_2b': []}, {'level_2c': []}, {'level_2c': []}, {'level_2c': []}, ]},
            {'level_2a': [{'level_2a': []}, {'level_2b': []}, {'level_2c': []}, ]},
            {'level_3a': [{'level_2a': []}, {'level_2b': []}, {'level_2c': []}, ]},
        ]}

        self.clear_widgets()
        self.add_widget(self.create_levels_recursively(level, 0))

    def create_levels_recursively(self, heatmap_goal_info, level):
        name, child_goals = list(heatmap_goal_info.items())[0]

        heatmap_goal = GoalHeatmap()
        heatmap_goal.name = name
        heatmap_goal.level = level
        for child_goal in child_goals:
            heatmap_goal.add_widget(self.create_levels_recursively(child_goal, level + 1))

        return heatmap_goal


class GoalHeatmap(BoxLayout):
    level: int = NumericProperty()
    name: str = StringProperty()
    from kivymd.uix.bottomnavigation import MDNavigationLayout


class Actions(MDBoxLayout):
    pass


class ActionsList(MDBoxLayout):
    pass
