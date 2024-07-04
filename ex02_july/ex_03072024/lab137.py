import os.path
file_path='vaishu.txt'
try:
    with open('vaishu.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfr:
    print('I am not able to find the file,please check the path')
finally:
    if os.path.isfile(file_path):
        print('Closing the file')