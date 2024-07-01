#using two arguments in functions
def allowed_to_attend_python_class(name,password):
    if name=='vaishnavi':
        if password=='yes':
            print('You are allowed enter')
    else:
        print('Not allowed')
allowed_to_attend_python_class('vaishnavi','yes')
allowed_to_attend_python_class('sriram','yes')
allowed_to_attend_python_class('sriram','no')
