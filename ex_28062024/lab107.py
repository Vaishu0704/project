class bankaccount:
    def __init__(self):
        self.balance=0
        self.__private_var=100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def show_balance(self):
        print('your balance',self.balance)

jp=bankaccount()
print(jp.balance)
jp.deposit(101)
jp.show_balance()
jp.deposit(99)
jp.show_balance()
jp.withdraw(50)
jp.show_balance()