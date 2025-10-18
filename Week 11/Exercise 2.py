class Person():
	pass

class Bus:
    def __init__(self, max_passengers):
        if max_passengers < 0:
            raise ValueError("Maximum passengers value can not be negative")
        
        self.max_passengers = max_passengers
        self.passengers = []

    def addPassenger(self, person:Person = Person()):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("The bus is full")

    def removePassenger(self):
        if len(self.passengers) > 0:
            self.passengers.pop()

if __name__ == '__main__':
    bus = Bus(5)

    for _ in range(6):
        bus.addPassenger()

    bus.removePassenger()

    print(len(bus.passengers))