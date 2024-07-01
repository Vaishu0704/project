#Hybrid inheritance
#Hierarchical mixed with single,multiple and multilevel
class A:
    def methoda(self):
        return 'Method A'

class B(A):
    def methodb(self):
        return 'Method B'
class C(A):
    def methodc(self):
        return 'Method C'
class D(B,C):
    def methodd(self):
        return 'Method D'

d=D()
print(d.methoda())
print(d.methodb())
print(d.methodc())
print(d.methodd())