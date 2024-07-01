class Father:
    def home(self):
        print('1 bBHK')

class Son(Father):
    def home(self):
        super().home() #to get parent class super() is used
        print('3 Bhk')

son=Son()
son.home()