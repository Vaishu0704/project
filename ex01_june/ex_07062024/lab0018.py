#List
#shopping list -milk,bread,butter,poha
s_list = ['milk', 'bread', 'butter', 'poha']
print(s_list)
print(len(s_list))
print(s_list[0])
print(s_list[-1])
#in list we can add,int,str,bool,complex,float
#to add
s_list.append('curd')
print(s_list)
#to add after index
s_list.insert(1, 'jam')
#extend is used to add another list at the end
s_list.extend(['chips', 'salt'])
print(s_list)
#to remove an item
s_list.remove('bread')
print(s_list)
print(s_list.index('jam'))
s_list.reverse()
s_list.sort()
print(s_list)
#print(s_list.pop())  #pop is last index

