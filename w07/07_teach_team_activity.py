import random

number = random.randint(1, 100)
user_input = -1

while number != user_input:
    user_input = int(input('What is your guess? '))
    if (user_input < number):
        print('Higher')
    else:
        print('Lower')

print('You guessed it!')