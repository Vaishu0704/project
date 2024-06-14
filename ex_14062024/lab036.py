#Range can be negative but it is not highly recommended
#for i in range(0,10,-1): range can't be 0 to 10 for negative
for i in range(10,0,-1):
    print(i)
for i in reversed(range(0,10)):
    print(i)