from datetime import datetime

class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date()

    @property
    def age(self):
        current_year = datetime.today().year
        current_month = datetime.today().month

        birth_year = self.date_of_birth.year
        birth_moth = self.date_of_birth.month

        age = current_year - birth_year

        if current_month < birth_moth:
            age -= 1

        return age

def only_adults(func):
        def wrapper(user:User):
            age = user.age
            if age < 18:
                raise ValueError(f'The user must be an adult, and you are {age} y.o')
            func(User)
        return wrapper

@only_adults
def buy_drugs(user:User):
    print('Your order number is AQWE12321')


if __name__ == '__main__':
    buy_drugs(User('12/10/1999'))

    try:
        buy_drugs(User('12/10/2009'))
    except ValueError as e:
        print(e)