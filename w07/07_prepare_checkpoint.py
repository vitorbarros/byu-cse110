user_number = -1

while user_number < 0:
    user_number = int(input('Please type a positive number: '))

kid_candy_parent_response = 'no'

while kid_candy_parent_response.lower() == 'no':
    kid_candy_parent_response = input('May I have a piece of candy? ')