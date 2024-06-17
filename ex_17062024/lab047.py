def say_hello():  #non return type with no parameter or arguments
    print('Hello')
say_hello()

def say_hello_arg(name): #non return type with argument
    print('Hello',name)
say_hello_arg('Vaishnavi')

def say_hello_default(name='Vaishnavi'): #non return type with default arguments
    print('Hello',name)
say_hello_default()
say_hello_default('Sriram')
say_hello_default(name='Haritha')
