class Person():
	pass

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def addPassenger(self, person:Person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("The bus is full")

    def removePassenger(self):
        if len(self.passengers) > 0:
            self.passengers.pop()