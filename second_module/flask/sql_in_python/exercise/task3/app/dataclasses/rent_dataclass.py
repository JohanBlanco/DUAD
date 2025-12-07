class Rent:
    def __init__(self, id=None, status="", car_id=None, user_id=None):
        self.id = id
        self.status = status
        self.car_id = car_id
        self.user_id = user_id

    @classmethod
    def from_dict(cls, data):
        valid_keys = cls().__dict__.keys()
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)

    @classmethod
    def convert_list_to_dict(cls, _list):
        return [item.__dict__ for item in _list]
