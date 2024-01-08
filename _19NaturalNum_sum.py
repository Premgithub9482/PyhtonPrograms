# Program to find sum of natural numbers

num = int(input('enter an integer number: '))

if num < 0:
    print('please enter a positive number')
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(f'sum of first {num} natural number is: {sum}')