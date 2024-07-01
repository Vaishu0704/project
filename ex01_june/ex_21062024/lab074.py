t=(12,34,56)
#to append
new_t=t+(4,)
print(new_t)
#convert to list for append
my_list=list(t)
print(my_list)
my_list.append(5)
new_t2=tuple(my_list)
print(new_t2)