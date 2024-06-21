t=('Thetesting academy','for','Thetesting academy')
print(set(t))
set1={1,2,3}
set2={4,5,6}
my_set=set2.update(set2,{7,8,9})
my_set=set1.union(set2)
print(my_set)
set3={1,2,3,4,5}
set4={4,5,6,7,8}
my_set1=set3.intersection(set4)
print(my_set1)
my_set1=set3.difference(set4)
print(my_set1)
my_set1=set4.difference(set3)
print(my_set1)