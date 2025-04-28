import uuid

class Task:
    def __init__(self, title, description='', priority='normal', due_date=None, completed=False, tag='personal', id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed
        self.tag = tag

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date,
            'completed': self.completed,
            'tag': self.tag,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data.get('id'),
            title=data.get('title', ''),
            description=data.get('description', ''),
            priority=data.get('priority', 'normal'),
            due_date=data.get('due_date', None),
            completed=data.get('completed', False),
            tag=data.get('tag', 'personal'),
        )
