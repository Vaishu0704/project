#without using Recursion
def sum_of_digits(n):
    sum_of_digits=0
    while n>0:
        sum_of_digits=sum_of_digits+n%10
        n=n//10
    return sum_of_digits

print(sum_of_digits(12345))