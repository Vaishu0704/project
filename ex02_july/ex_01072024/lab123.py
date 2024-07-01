#Abstraction
#Hiding the details and showing what is required
#with different classes
from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def sound(self):
        pass
class Dog(animal):
    def sound(self):
        return 'Bark'
class Cat(animal):
    def sound(self):
        return 'Meow'

dog=Dog('Rancho')
print(dog.sound())
cat=Cat('Cat')
print(cat.sound())