#we can have multiple decorator
def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper
def decorator2(a):
    def wrapper():
        print('Decorator2')
        a()
    return wrapper
@decorator1
@decorator2
def say_hello():
    print('Say hello!!')
say_hello()
