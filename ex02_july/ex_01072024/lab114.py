#Multiple inheritance
#some feature from father and some feature from mother

class father:
    def father_money(self):
        return '5'
    def home(self):
        return 'This is from father'

class mother:
    def mother_money(self):
        return '10'
    def home(self):
        return 'This is from mother'
class Son(father,mother):
    pass
  #  def home(self):
   #     return 'This is from son'
son=Son()
print(son.home()) #it will take 1st argument father without pass in son
# it will take local(Method Resolution order MRO)
print(son.father_money())
print(son.mother_money())