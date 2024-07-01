#Encapsulation
#Bind the data variables with the methods
#Data members/class variables
#methods - def functions within the class
#wrapping or binding the data variable with the methods -Encapsulation
#Hide the data members(class variable/instance variable) by using methods

class car:
    name=None
    password='123'
    def __init__(self):
        print('I am called when object is created')

    def change_password(self):
        self.password='345'

xuv=car()
xuv.change_password()