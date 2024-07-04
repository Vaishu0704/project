#file io (to read the txt file)
with open('vaishu.txt','r') as file:
    print(file.read())
    file.close()
