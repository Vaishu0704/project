#os module
import os
import math

print(os.name) #os name
print(os.getcwd())#get current working dir
print(math.pi)
#to change dir
print(os.chdir(r'C:\Users\91915\PycharmProjects\project\ex02_july\ex_03072024'))
print(os.getcwd())
#to get a list of dir
print(os.listdir(r'C:\Users\91915\PycharmProjects\project\ex02_july\ex_03072024'))
#to make dir
os.mkdir('vaishu')
print(os.listdir())