# Sum of digits using recursion
def sum_of_digits(n):
    # Base case
    if n < 10:
        return n
    #Recursion case
    else:
        return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(12345))
