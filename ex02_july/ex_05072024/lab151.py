import os.path

size=os.path.getsize('testingdata.txt')
print(size)
if size!=0:
    print('File exist and has content')
else:
    print('File dont exist and no content')