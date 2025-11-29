class Task:
    def __init__(self, id = None, title = "", description = "", status = ""):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def convert_to_dict_list(task_List):
        return [task.__dict__ for task in task_List]