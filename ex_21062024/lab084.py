my_dict={'a':1,'b':2,'c':3,'a':98}
print(my_dict) #keys should be unique if ther is same keys latest one is taken
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
for i in list(my_dict.keys()):
    print(i)
for k,v in my_dict.items():
    print(k,v)