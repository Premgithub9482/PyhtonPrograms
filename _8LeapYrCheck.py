# program to check leap year

year = int(input('enter a year to check leap year or not: '))

if (year%400 == 0) and (year%100 == 0):
    print(f'the entered year {year} is a leap year')
elif (year%4 == 0) and (year%100 != 0):
    print(f'the entered year {year} is a leap year')
else:
    print(f'the entered year {year} is not a leap year')