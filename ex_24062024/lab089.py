#Map
#pick 1 item and apply the function
#give the same no.of elements
numbers=[1,2,3,4,5,6,7,8,9,10]
def double_me(num):
    return num*2
#double_me=lambda n:n*2
new_double=map(double_me,numbers)
print(list(new_double))

#Filter
#only works with function True or False
#pick item m if True keeps it,False removes it
#it gives less no.of items

def even_giver(num):
    return num%2==0
#even_giver=lambda n:n%2==0
new_even=filter(even_giver,numbers)
print(list(new_even))