class bankaccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print('your balance', self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print('Not allowed')

    def if_you_are_auth_user(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print('Not allowed')


jp = bankaccount()
jp.deposit(101)
secret_pwd = input('Enter the password to show balance')
if secret_pwd == '1234':
    jp.if_you_are_auth(True)
else:
    jp.if_you_are_auth(False)

secret_pwd = input('Enter the password for withdrawal')
if secret_pwd == '1234':
    jp.if_you_are_auth_user(True, 50)
else:
    jp.if_you_are_auth_user(False,50)

jp.if_you_are_auth(True)
