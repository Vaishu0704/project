try:
    num1=int(input('Enter the num1\n'))
    num2=int(input('Enter the num2\n'))
    result=num1/num2
    print(result)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'result is',{result})
finally:
    print('I will executed anyhow')
