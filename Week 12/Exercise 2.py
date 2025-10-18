from abc import ABC, abstractmethod 
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius: float):
        super().__init__()

        if radius < 0:
            raise ValueError("The radius can not be negative")
        
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * math.pow(self.radius, 2) 

class Square(Shape):

    def __init__(self, side_length:float):
        super().__init__()

        if side_length < 0:
            raise ValueError("The side length can not be negative")

        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length
    
    def calculate_area(self):
        return math.pow(self.side_length,2)

class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__()

        if length < 0 or width < 0:
            raise ValueError("The values can not be negative")

        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.width
    
    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    circle = Circle(radius=5)
    square = Square(side_length=4)
    rectangle = Rectangle(width=3, length=6)

    print("Circle:")
    print("  Area:", circle.calculate_area())
    print("  Perimeter:", circle.calculate_perimeter())

    print("\nSquare:")
    print("  Area:", square.calculate_area())
    print("  Perimeter:", square.calculate_perimeter())

    print("\nRectangle:")
    print("  Area:", rectangle.calculate_area())
    print("  Perimeter:", rectangle.calculate_perimeter())
