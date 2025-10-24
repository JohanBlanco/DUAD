import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("The radius can not be negative")

        self.radius = radius

    def get_area(self):
        return math.pi * math.pow(self.radius,2)
    
if __name__ == '__main__':
    try:
        circle = Circle(-5)
    except ValueError as valueError:
        print(valueError)

    circle = Circle(3)
    print(circle.get_area())

