class Car:
    def __init__(self, id=None, vin = "", make="", model="", year=None, status=""):
        self.id = id
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.status = status

    @classmethod
    def from_dict(cls, data):
        valid_keys = cls().__dict__.keys()
        filtered = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered)

    @classmethod
    def convert_list_to_dict(cls, _list):
        return [item.__dict__ for item in _list]

