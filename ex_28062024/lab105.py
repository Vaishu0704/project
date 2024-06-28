class myclass:
    def __init__(self):
        self.name='Amit'
        self.__email='amit@gmail.com'

    def public_func(self):
        print('Public function')

    def __private_func(self):
        print('This is private')

    def public_fn_private(self):
        self.__private_func()
        print(self.__email)

a=myclass()
a.public_func()
a.public_fn_private()