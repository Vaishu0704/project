#list-collection of items
num=[1,2,3]
def do_something(num): #3rd define function executes
    num.append(4)
    num[0]=100
    return num
num.append(10) #first execution
l=do_something(num) #second call function executes
print(l)