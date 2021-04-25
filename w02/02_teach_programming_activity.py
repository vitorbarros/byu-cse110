print('Please enter the following information:\n')

# user inputs
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')

# formatting values as needed
first_name_formatted = first_name.capitalize()
last_name_formatted = last_name.upper()
email_address_formatted = email_address.lower()
job_title_formatted = job_title.capitalize()

# preparing card information
line_1 = f'{last_name_formatted}, {first_name_formatted}'
line_2 = job_title_formatted
line_3 = f'ID: {id_number}\n'
line_4 = email_address_formatted
line_5 = phone_number

divider = '----------------------------------------'

# output
print('\nThe ID Card is:')
print(divider)
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(divider)







