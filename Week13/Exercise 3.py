import datetime

class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y").date()

    @property
    def age(cls, self):
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month

        birth_year = self.date_of_birth.year
        birth_moth = self.date_of_birth.month

        age = current_year - birth_year

        if current_month < birth_moth:
            age -= 1

        return age
    
def decorator(func):
        def wrapper(*parameters):
            print(f"Parameters from Wrapper before the function: {parameters}")
            func(parameters)
            print(f"Parameters from Wrapper after the function: {parameters}")
        return wrapper
