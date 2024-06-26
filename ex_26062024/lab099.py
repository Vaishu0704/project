#user input
class student:
    def __init__(self):
        self.name=input('Enter the name')
        self.age=input('Enter the age')

    def display(self):
        print(f'Name is {self.name} and age is {self.age}')

student=student()
student.display()