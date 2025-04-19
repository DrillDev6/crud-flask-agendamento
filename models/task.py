class Task:
    def __init__(self, id, title, descriptions, completed):
        self.id = id
        self.title = title
        self.descriptions = descriptions
        self.completed = completed
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "descriptions": self.descriptions,
            "completed": self.completed
        }

    
    