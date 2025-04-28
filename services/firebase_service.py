import firebase_admin
from firebase_admin import credentials, db
from config.settings import FIREBASE_CREDENTIALS, FIREBASE_DATABASE_URL

# Inicializar Firebase
cred = credentials.Certificate(FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DATABASE_URL
})

def save_task(task):
    ref = db.reference('/tasks')
    new_task_ref = ref.push()
    new_task_ref.set(task.to_dict())

def get_tasks():
    ref = db.reference('/tasks')
    return ref.get()

