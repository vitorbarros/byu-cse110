print('Enter a list of numbers, type 0 when finished.')

numbers_list = []

number = -1

while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers_list.append(number)

total = sum(numbers_list)
average = sum(numbers_list) / len(numbers_list)
largest = max(numbers_list)

print(f'The sum is: {total}')
print(f'The average is: {average}')
print(f'The largest number is: {largest}')

