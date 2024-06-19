my_list=[1,2,3]
#Indexing
print('Element at index 0:',my_list[0])
#changing an element
my_list[1]=20
print('list after changing an element at index 1:',my_list)
#append
my_list.append(4)
print('list of element after appending:',my_list)
#extend
my_list.extend([5,6])
print('List of element after extending:',my_list)
#insert
my_list.insert(2,'e')
print('list of element after inserting:',my_list)
#remove
my_list.remove('e')
print('List of elements after removing e:',my_list)
#copy
my_copylist=my_list.copy()
print(my_copylist)
my_list.clear()
print('Invalid list',my_list)
print(my_copylist)
#print('Index of 3 in the list',my_list.index(3)) #there is no occurence of 3
my_copylist.sort()
print(my_copylist)
my_copylist.reverse()
print(my_copylist)