import os
#to list all dir
all_dir=os.listdir(r'C:\Users\91915\PycharmProjects\project\ex02_july\ex_03072024')
print(all_dir)
os.environ['My_var']='sriram'  #creating environment variable
print(os.getenv('My_var'))
#walk me in the dir
for root,dir,files in os.walk(r'C:\Users\91915\PycharmProjects\project\ex02_july'):
    print(f'current dir {root}')
    print(f'sub dir dir{dir}')
    print(f'files dir dir{files}')
    print(len(files))