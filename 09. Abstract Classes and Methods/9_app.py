# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that 
# implements area().


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width
    

R1 = Rectangle(10, 20)

print(R1.area())
        

