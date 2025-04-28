from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.tasks = []  # Lista de tareas

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text='Bienvenido a Bullet Planner')
        self.add_task_button = Button(text='Agregar nueva tarea', on_press=self.go_to_add_task)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.add_task_button)

        self.add_widget(self.layout)

    def go_to_add_task(self, instance):
        self.manager.current = 'edit_task'

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarea agregada: {task.title}")