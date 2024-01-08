# Program to find factorial a number

# using loop
num = int(input('enter an integer number: '))

fact = 1
if num < 0:
    print('factorial of value less than 0 does not exist')
else:
    for i in range(1,num+1):
        fact *= i
    print('factorial of ',num,' is: ',fact)

# Using recursion function
def fact(n):
    if n < 0:
        pass
    else:
        return (n*fact(n-1))
result = fact(num)
print('factorial of given number is: ',result)