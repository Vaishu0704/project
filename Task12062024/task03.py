# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
fact=1
n=int(input('Enter the number\n'))
for i in range(1,n+1):
    fact=fact*i
print('factorial of n is',fact)