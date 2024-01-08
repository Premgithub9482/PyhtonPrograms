# Program to check prime number

num = int(input('enter a integer number to check prime or not: '))

if num == 1:
    print('the entered number is not a prime number')

if num>1:
    for i in range(2,num):
        if num%i == 0:
            print('the entered number is not a prime number')
            break
    # else part outside of for block to recognise num 2 is a prime
    else:
        print('the entered number is prime number')