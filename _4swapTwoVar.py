# swapping two variables in python

# by storing in temp variable(third variable)
var1 = 10
var2 = 20
print(f'the value of first_variable is before swapping - {var1} \nthe value of second_variable is before swapping - {var2}')

temp_var = var1
print()

var1 = var2
print(f'the value of first_variable is after swapping - {var1}')

var2 = temp_var
print(f'the value of second_variable is after swapping - {var2} \n')


# without using third variable
var1 = 1
var2 = 2
print(f'the value of var1 before swap - {var1}\nthe value of var2 before swap - {var2}\n')

var1, var2 = var2, var1
print(f'the value of var1 after swap - {var1}\nthe value of var2 after swap - {var2}')