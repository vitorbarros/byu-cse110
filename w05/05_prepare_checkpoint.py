import math

a = input('Please enter your favorite number:')
a = int(a)
b = input('Please enter your next favorite number:')
b = int(b)

if (a) > (b):
    print('Your first number is greater.\n'
          'The numbers are not equal.\n'
          'Your second number is lower.')

elif (a) < (b):
    print('Your first number is not greater.')

elif (a) == (b):
    print('Your two favorite numbers are the same.')
    print('The first number is not greater.\n'
          'The second number is not greater')

if (a) < (b):
    print('Your second number is greater\n'
          'The numbers are not equal.')

animal = input('Please enter your favorite animal:')
animal = animal.lower()

if animal == 'elephant':
    print('That is my favorite animal too!')
else:
    print('That one is not my favorite animal')
