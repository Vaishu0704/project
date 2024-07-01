class calc:
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

object_ref=calc()
output=object_ref.sum(3,4)
print(output)
output1=object_ref.sub(3,4)
print(output1)
output2=object_ref.mul(3,4)
print(output2)
output3=object_ref.div(3,4)
print(output3)