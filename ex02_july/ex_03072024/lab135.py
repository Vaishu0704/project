import os.path

try:
    file = open('example.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfr:
    print('I am not able to find the file,please check the path')
finally:
    print('Executed')
try:
    file.close()
except NameError as ne:
    print(ne)
