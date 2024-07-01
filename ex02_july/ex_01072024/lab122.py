class mathutils(object):
    def add(self,a,b=0,c=0):
        return a+b+c
math=mathutils()
op1=math.add(1)
op2=math.add(1,2)
op3=math.add(1,2,3)
print(op1)
print(op2)
print(op3)
#Method overloading is supported only with default arguments