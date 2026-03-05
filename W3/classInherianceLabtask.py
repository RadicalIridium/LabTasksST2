"""
Class Inheritance Lab Task 
Task to develop a Python program that creates shapes using object-oriented inheritance hierarchy.

"""

from abc import ABC, abstractmethod
import math

#Task 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
#Task 2, 3, 4, 5
class Shape(ABC):
    def __init__(self):
        self.points = []

    
    @abstractmethod
    def calculatePoints(self):
        pass

    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass

    def move(self):
        moveinput = input("Move object to new coordinate (leftTop) (x y): ")
        cords = moveinput.split()
        self.leftTop = Point(int(cords[0].strip()), int(cords[1].strip()))
        self.calculatePoints()


# Task 6
class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        userinput = input("Coordinate(LeftTop), height and width  (x y height width): ")
        cords = userinput.split()

        self.leftTop = Point(int(cords[0].strip()), int(cords[1].strip()))
        self.height = int(cords[2].strip())
        self.width = int(cords[3].strip())

    def calculatePoints(self):
        self.points = []

        topLeft = self.leftTop
        topRight = Point(self.leftTop.x + self.width, self.leftTop.y)
        bottomRight = Point(self.leftTop.x + self.width, self.leftTop.y + self.height)
        bottomLeft = Point(self.leftTop.x, self.leftTop.y + self.height)

        self.points = [topLeft, topRight, bottomRight, bottomLeft]
    
    def calculateArea(self):
        return self.height * self.width
    
    def calculatePerimeter(self):
        return 2 * (self.height + self.width)


class Circle(Shape):
    def __init__(self):
        super().__init__()
        userinput = input("Coordinate(LeftTop), and radius (x y radius): ")
        cords = userinput.split()

        self.leftTop = Point(int(cords[0].strip()), int(cords[1].strip()))
        self.radius = int(cords[2].strip())

    def calculatePoints(self):
        self.points = []

        topleft = self.leftTop
        bottomright = Point(self.leftTop.x + self.radius * 2, self.leftTop.y + self.radius * 2)
        
        self.points = [topleft, bottomright]

    def calculateArea(self):
        return math.pi * self.radius ** 2
    
    def calculatePerimeter(self):
        return 2 * math.pi * self.radius
    

commandloop = True
print("#####" * 20)
while commandloop == True:
    usercommand = input("Type of Shape (q for exit, r for rectangle, c for circle): ")
    if usercommand == "q":
        print("#####" * 20)
        commandloop = False
    elif usercommand == "r":
        print("-- Rectangle --") 

        rectangle = Rectangle()
        rectangle.calculatePoints()
        print("Height:", rectangle.height)
        print("Width:", rectangle.width)
        print("Left Top:", rectangle.leftTop)
        print("Area:", rectangle.calculateArea())
        print("Perimeter:", rectangle.calculatePerimeter())
        print("Points:", " ".join(str(point) for point in rectangle.points))

        # Move Prompt
        rectangle.move()

        print("-- Rectangle --") 
        rectangle.calculatePoints()
        print("Height:", rectangle.height)
        print("Width:", rectangle.width)
        print("Left Top:", rectangle.leftTop)
        print("Area:", rectangle.calculateArea())
        print("Perimeter:", rectangle.calculatePerimeter())
        print("Points:", " ".join(str(point) for point in rectangle.points))

    elif usercommand == "c":
        print("-- Circle --") 

        circle = Circle()
        circle.calculatePoints()
        print("Radius:", circle.radius)
        print("Left Top:", circle.leftTop)
        print("Area:", circle.calculateArea())
        print("Perimeter:", circle.calculatePerimeter())
        print("Points:", " ".join(str(point) for point in circle.points))

        # Move Prompt
        circle.move()

        print("-- Circle --") 
        circle.calculatePoints()
        print("Radius:", circle.radius)
        print("Left Top:", circle.leftTop)
        print("Area:", circle.calculateArea())
        print("Perimeter:", circle.calculatePerimeter())
        print("Points:", " ".join(str(point) for point in circle.points))


