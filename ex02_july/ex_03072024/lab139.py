#To create our own exception
class MyCustomException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message) #parent(Exception) constructor
balance=100
try:
    withdraw=int(input('Enter the amount'))
    if withdraw>balance:
        raise MyCustomException ('Balance is low!') #raise used when the condition is fulfilled
    else:
        print('Remaining balance',(balance-withdraw))
except MyCustomException as e:
    print(e)
except ValueError as ve:
    print(ve)
