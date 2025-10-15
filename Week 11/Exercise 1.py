import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        math.pi * math.pow(self.radius,2)
