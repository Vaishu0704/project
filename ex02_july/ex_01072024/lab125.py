from abc import ABC,abstractmethod
class pyatb(ABC):
    @abstractmethod
    def payfee(self):
        pass
    def enrolled(self):
        print('Enrolled')

class Vaishu(pyatb):
    def payfee(self):
        print('payed')
vaish=Vaishu()
vaish.payfee()