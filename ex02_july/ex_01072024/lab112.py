#Hierarchical inheritance
#one father multiple children i.e multiple derived classes
#inherited from single class
class father:
    def bhk1(self):
        print('1 BHK')

class Vaishnavi(father):
    def bhk2(self):
        print('2 Bhk')

class Haritha(father):
    def bhk3(self):
        print('3 BHk')

class Janani(father):
    def no_house(self):
        print('No house')

vaishnavi=Vaishnavi()
vaishnavi.bhk2()
vaishnavi.bhk1()

haritha=Haritha()
haritha.bhk3()
haritha.bhk1()

janani=Janani()
janani.no_house()
janani.bhk1()