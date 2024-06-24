#Recursion
#programming technique when a function calls
#itself in order to solve a problem
#key concepts
#1.Base case
#2.Recursion case
#Factorial program
#n=5
#for i in range(1,n+1):
def factorial(n):
    #Base case
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))