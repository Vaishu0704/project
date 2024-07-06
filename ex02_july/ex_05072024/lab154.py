import os
fd=os.open('testingdata.txt',os.O_RDWR)
os.write(fd,b'Hello I am writing')
os.close(fd)
