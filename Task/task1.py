#Explain the difference between the = operator and the == operator in Python.
# = - assigned operator
a=29
name='Vaishnavi'
# == -comparison operator
x=5
y=29
print(a==x)
print(a==y)

#What does the ** operator do in Python, and how is it used?
#** is an exponential operator or power operator
c=4
d=2
print(c**d)

#What does the ^ operator do in Python, and in what context is it commonly used?
# ^ - XOR(used in bitwise operator and swapping)
a=10
b=3
print(a^b)
print(a)
print(b)
#swapping variables
a=a^b #a^b is stored in a
b=a^b #newa^b and stored in b
a=a^b # a^new b and stored in a
print(a)
print(b)