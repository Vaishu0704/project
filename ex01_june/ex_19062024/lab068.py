my_list=[1,2,3,4,5]
#def double_item(num):
 #   return num*2
double_item=lambda num:num*2
#using map function
double_list=list(map(double_item,my_list))
print(double_list)
