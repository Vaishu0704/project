from abc import ABC,abstractmethod
class father(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass
class Vaishnavi(father):
    def loan(self):
        #pass  #pass should not given in child class
        print('Loan from father') #i.e the child should forcibly return some value
        # since parent is incomplete

vaish=Vaishnavi('Giri')
vaish.loan()