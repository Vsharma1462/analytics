from abc import ABC,abstractmethod

# abstract class
class shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# creating subclass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)  

    def perimeter(self):
        return 2 * 3.14 * self.radius
    

class rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height=height

    def area(self):
        return (self.height * self.width)  

    def perimeter(self):
        return 2*(self.width + self.height)
    
#circle1=circle(5)
#print(circle1.area())    
#print(circle1.perimeter())
shapes = [circle(5) , rectangle(4,5)  ]    
for shape in shapes:
    print(f"area : {shape.area()}")
    print(f"perimeter : {shape.perimeter()}")

        