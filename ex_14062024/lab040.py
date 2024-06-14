#match case can be used for both numbers and strings
name=input('Enter a name\n')
match name:
    case 'vaishnavi':
        print('you are vaishnavi')
    case 'sriram':
        print('you are sriram')
    case _:
        print('No idea')