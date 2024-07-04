class Parent:
    def __init__(self):
        print('I am parent')
class Son(Parent):
    def __init__(self):
        super().__init__()
son=Son()
