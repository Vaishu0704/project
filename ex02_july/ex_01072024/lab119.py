#Polymorphism
#Allow object of different classes to be treated as
#object of a common superclass
#i.e they will act differently in different situation
#Method overloading doesn't exist in python
#Method overriding

class shape:
    def area(self):
        print('Area of the shape')
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

shape1=rectangle(3,4)
print(shape1.area())
shape2=circle(10)
print(shape2.area())
#same name in parent and child but child always overrides the parent