# Program to find Armstrong numbers in an interval

lower = int(input('enter lower interval number: '))
upper = int(input('enter upper interval number: '))
Armstng_numrs = []

for num in range(lower,upper+1):
    ln = len(str(num)) # to find length of num
    temp = num
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum += rem**ln
        temp //= 10
    if sum == num:
        Armstng_numrs += [sum] # appending armstrong num to list(Armstng_nums.append(sum))
print('Armstrong numbers are: ',Armstng_numrs) 

