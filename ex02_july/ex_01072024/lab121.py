#Method overloading
#doesnot support in the traditional sense
class mathutils:
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,c):
        return a+c
math=mathutils()
op1=math.add(4,3) #it does only latest add
print(op1)
op2=math.add(4,2) #it does latest add
print(op2)