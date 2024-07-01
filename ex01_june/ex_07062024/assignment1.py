#All functions in list
#append
list=[1,2,3]
list.append(4)
print(list)
#extend
list.extend([4,5,6])
print(list)
#insert
list.insert(1,'e') #inserting 'e' in 1st index
print(list)
#remove
list.remove(2) #removing 2 in the list
print(list)
#pop (by default removes the last num in the list) i.e with no index
item=list.pop(1)
print(item)
print(list)
#index (returns the first occurence of the repeated value
index=list.index(4)
print(index)
#count(returns the number of occurence of a specified value)
count=list.count(4)
print(count)
#reverse
list.reverse()
print(list)
#sort
list.sort()
print(list)
#copy
new_list=list.copy()
print(new_list)
#clear (removes all the element from the list)
new_list.clear()
print(new_list)
#length
l=len(list)
print(l)
