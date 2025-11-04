class Category:
    def __init__(self, category='', color=''):
        self.category = category
        self.color = color

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_matrix(self):
        return self.category

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.to_dict() == other.to_dict()