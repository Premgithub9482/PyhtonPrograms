# Program to print all prime numbers in an interval

lower = int(input('enter lower limit here: '))
upper = int(input('enter upper limit here: '))

for prime in range(lower, upper + 1):
    if prime > 1:
        for j in range(2,prime):
            if prime%j == 0:
                break
        else:
            print(prime)
            