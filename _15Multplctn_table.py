# Program to print Multiplication table

# Using for loop
num = int(input('enter the number to show the multiplication table: '))

for i in range(11):
    result = num*i
    print(f'{num} * {i} = {result}')
print()


# Using while loop
n = 0
while n <= 10:
    result = num*n
    print(f'{num} * {n} = {result}')
    n += 1