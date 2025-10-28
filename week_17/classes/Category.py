class Category:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)