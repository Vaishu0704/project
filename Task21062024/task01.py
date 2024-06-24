# Right Triangle Star Pattern
n = 5
for i in range(1, n + 1):
    print('*' * i)
#Left Triangle star pattern
for j in range(1, n + 1):
    print(' ' * (n - j) + '*' * j)
