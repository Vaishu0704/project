try:
    a=int(input('Enter the num1\n'))
    b=int(input('Enter the num2\n'))
    c=a/b
    print('Result is',c)
except Exception as e:
    print(e)
    print('Please enter integer')
print('End of the program')