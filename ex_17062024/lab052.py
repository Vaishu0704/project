#*args (similar to list with no.of arguments)
def print_argument(*args):
    for i in args:
        print(i,end='\n')
print_argument('Vaishnavi','Sriram','Yashwanth Sai')