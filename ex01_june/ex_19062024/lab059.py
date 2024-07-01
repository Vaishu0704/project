#lambda expression--to do the task in one line
def double_mysalary(salary):
    return salary*2
new_salary=double_mysalary(100)
print(new_salary)
#in lambda
f_double_salary=lambda salary:salary*2
print(f_double_salary(200))