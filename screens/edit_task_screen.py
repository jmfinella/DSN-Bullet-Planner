from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from models.task import Task

class EditTaskScreen(Screen):
    def __init__(self, **kwargs):
        super(EditTaskScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_input = TextInput(hint_text="Título de la tarea", multiline=False)
        self.save_button = Button(text="Guardar Tarea", on_press=self.save_task)

        self.layout.add_widget(self.title_input)
        self.layout.add_widget(self.save_button)

        self.add_widget(self.layout)

    def save_task(self, instance):
        title = self.title_input.text.strip()
        if title:
            new_task = Task(title=title)
            # Guardamos la tarea en una lista local (por ahora)
            self.manager.get_screen('home').add_task(new_task)
            # Volvemos al home
            self.manager.current = 'home'
            # Limpiamos el campo de texto
            self.title_input.text = ''
