#swwitch in JAVA but match case in python
numbers=int(input('Enter the number\n'))
match numbers:
    case 1:
        print('You are entered 1')
    case 2:
        print('You are entered 2')
    case 3:
        print('You are entered 3')
    case 4:
        print('You are entered 4')
    case 5:
        print('You are entered 5')
    case _:
        print('No idea')