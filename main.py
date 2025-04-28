from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.home_screen import HomeScreen
from screens.edit_task_screen import EditTaskScreen

class BulletPlannerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(EditTaskScreen(name='edit_task'))
        return sm

if __name__ == '__main__':
    BulletPlannerApp().run()
