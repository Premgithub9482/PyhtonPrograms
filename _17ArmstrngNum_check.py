# Program to check Armstrong number (153) = (1*1*1) + (5*5*5) + (3*3*3) = 153

num = int(input('enter a number: '))

ln = len(str(num))
temp = num
sum = 0
while temp > 0:
    rem = temp%10
    sum += rem**ln
    temp //= 10
if num == sum:
    print(f'Given number {num} is a Armstrong number')
else:
    print(f'Given number {num} is not a Armstrong number')