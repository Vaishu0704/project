class car:
    name=None

    def __init__(self):
        self.public_var='public'
        self._protected_var='protected123'
        self.__private_var='123'

    def __private_method(self):
        print('protected')

    def print_name(self):
        self.__private_method()
        if self.__private_var=='123':
            print('Hi,123')
        print('I am alllowed public')

auto=car()
auto.print_name()