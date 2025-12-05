class User:
    def __init__(self,id = None,first_name = "",last_name = "",email="", username = "",password = "", birthdate = "", status = ""):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.birthdate = birthdate
        self.status = status

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def convert_list_to_dict(cls, _list):
        return [item.__dict__ for item in _list]
