#Constructor
#It is a special method that is automated when the object is called from the class
#used to initialize the values of the instance variable(Attributes)
#2 types of constructor
#default and constructor with parameters
class Dog:
    name=None
    id=None

    def __init__(self):  #default constructor
        print('Default no arguments')

    def __init__(self,name,id):  #constructor with parameter
        self.name=name
        self.id=id

    def sleep(self):
        print('Sleeping',self.name)

dog1=Dog('Chow','1')
dog2=Dog('Mow','2')
print(f'{dog1.name}has Id {dog1.id}')
print(f'{dog2.name}has Id {dog2.id}')
dog1.sleep()
dog2.sleep()
