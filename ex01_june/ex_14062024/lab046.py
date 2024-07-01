#using match cases
def allowed_to_attend_python_class(name):
    match name:
        case 'vaishnavi':
            print('vaishnavi is allowed')
        case 'sriram':
            print('sriram is allowed')
        case _:
            print('Not allowed')
allowed_to_attend_python_class('vaishnavi')
allowed_to_attend_python_class('sriram')
allowed_to_attend_python_class('haritha')