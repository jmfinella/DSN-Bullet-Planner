from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from tinydb import TinyDB, Query

# Inicializar la base de datos
db = TinyDB('db.json')
tasks_table = db.table('tasks')
Task = Query()

class TaskItem(BoxLayout):
    def __init__(self, task_id, text, completed=False, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=40, **kwargs)
        self.task_id = task_id  # Guardamos el ID de la tarea
        self.checkbox = CheckBox(active=completed)
        self.checkbox.bind(active=self.on_checkbox_active)
        self.label = Label(text=text, halign="left", valign="middle")
        self.add_widget(self.checkbox)
        self.add_widget(self.label)

    def on_checkbox_active(self, checkbox, value):
        tasks_table.update({'completed': value}, doc_ids=[self.task_id])
        if value:
            print(f"✅ Tarea '{self.label.text}' marcada como completada.")
        else:
            print(f"🔄 Tarea '{self.label.text}' marcada como pendiente.")

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.scroll = ScrollView()
        self.task_list = GridLayout(cols=1, size_hint_y=None)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.scroll.add_widget(self.task_list)
        self.add_widget(self.scroll)

        # Text input para nueva tarea
        self.input_box = BoxLayout(size_hint_y=0.1)
        self.task_input = TextInput(hint_text="Escribe una nueva tarea...")
        self.add_task_button = Button(text="Agregar")
        self.add_task_button.bind(on_release=self.add_task)
        self.input_box.add_widget(self.task_input)
        self.input_box.add_widget(self.add_task_button)
        self.add_widget(self.input_box)

        # Botón de sincronizar (todavía no implementado)
        self.sync_button = Button(text="Sincronizar", size_hint_y=0.1)
        self.add_widget(self.sync_button)

        # Cargar tareas existentes
        self.load_tasks()

    def load_tasks(self):
        self.task_list.clear_widgets()
        for item in tasks_table.all():
            task = TaskItem(task_id=item.doc_id, text=item['text'], completed=item.get('completed', False))
            self.task_list.add_widget(task)

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            # Guardar en base de datos
            new_task = tasks_table.insert({'text': task_text, 'completed': False})
            print(f"➕ Nueva tarea agregada: '{task_text}'")

            # Mostrar en pantalla
            task = TaskItem(task_id=new_task, text=task_text)
            self.task_list.add_widget(task)

            # Limpiar el input
            self.task_input.text = ""

class BulletApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    BulletApp().run()