import os.path
file_path='ex.txt'
try:
    with open('ex.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as fnfr:
    print('I am not able to find the file,please check the path')
finally:
    if os.path.isfile(file_path):
        print('Closing the file')