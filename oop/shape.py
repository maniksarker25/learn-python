from math import pi
class Shape:
    def __init__(self,name):
        self.name = name
    
class Rectangle(Shape):
    def __init__(self, name,length,width):
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        print(self.length * self.width) 
    

class Circle(Shape):
    def __init__(self, name,redius):
        self.redius = redius
        super().__init__(name)
    
    def area(self):
        print(pi * self.redius* self.redius)
    

rectangle = Rectangle("Rectangle",10,23)
rectangle.area()
circle = Circle("circle",33)
circle.area()
