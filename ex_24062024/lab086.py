my_dict = {'b': 2, 'a': 1, 'c': 3}
# for iterate
for k, v in my_dict.items():
    if k == 'b':
        print('Key with the name b is found')

op = 'b' in my_dict  # in built-in function to identify a value
print(op)
