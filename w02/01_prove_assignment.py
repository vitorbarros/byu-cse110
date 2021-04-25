# user inputs

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

first_name_formatted = first_name.capitalize()
last_name_formatted = last_name.capitalize()

result = f'Your name is {last_name_formatted}, {first_name_formatted} {last_name_formatted}.'

print(result)