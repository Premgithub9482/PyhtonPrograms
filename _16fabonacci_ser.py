# Program to print the Fabonacci sequence

x = 0
y = 1
num = int(input('enter the number to obtain fabonacci sequence: '))

for i in range(num):
    print(x,end=' ')
    temp = x
    x = y
    y = temp + x
print()


x,y = 0,1
for i in range(num):
    print(x,end=' ')
    x,y=y,x+y