# Program to generate a random number

import random

while True:
    choice = (input('press "1" To generate random number between 1 to 100\npress "2" To exit program\nEnter choice: '))
    num = random.randint(1,100)
    if choice == '1':
        print(f'randomly genrated num is: {num}')
    elif choice == '2':
        break
    else:
        print('invalid choice')
    