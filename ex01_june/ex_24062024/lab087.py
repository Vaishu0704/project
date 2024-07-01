#Filters in python
#The filter() fn in python is a built-in
#allows you to filter the elements in the list,tupple,set
numbers=[1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    return num%2==0

new_num_even=filter(is_even,numbers)
print(list(new_num_even))