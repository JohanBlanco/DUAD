from abc import ABC

class Athlete(ABC):
    pass

class Runner(Athlete):

    def run(self):
        print("I'm running...")

class Swimmer(Athlete):

    def swim(self):
        print("I'm swimming...")

class Cyclist (Athlete):

    def ride(self):
        print("I'm riding a bike...")

class Triathlete(Runner, Swimmer, Cyclist):

    def workout(self):
        self.ride()
        self.swim()
        self.run()

if __name__ == '__main__':
    triathlete = Triathlete()
    triathlete.workout()