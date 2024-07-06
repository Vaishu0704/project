#Get file modification time
import os.path
import time

mtime=os.path.getmtime('testingdata.txt')
print(mtime) #o/p in epoch time
#to convert epoch time to normal time
print(time.gmtime(mtime))
print(time.localtime())
