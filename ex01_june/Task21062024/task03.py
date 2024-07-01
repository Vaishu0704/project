#String Reverse
#1st method
name=input('Enter the name\n')
a=name[::-1]
print(a)
#2nd method
t=list(name)
t.reverse()
t=''.join(t)
print(t)
#3rd method
e=''.join(reversed(name))
print(e)
#4th method
f=""
for i in name:
    f=i+f
print(f)

