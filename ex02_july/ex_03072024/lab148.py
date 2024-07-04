#to overcome lines in a list,use for loop
with open('Testdata.txt','r') as file:
#print(lines)

    for line in file:
        print(line,end='')