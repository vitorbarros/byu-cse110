import os

# preparing file path
file_name = 'life-expectancy.csv'
current_path = os.path.dirname(__file__)
file_path = f'{current_path}/{file_name}'

entity = []
entity_code = []
year = []
life_expectancy = []

# preparing data
with open(file_path) as life_expectancy_data:
    for index, line in enumerate(life_expectancy_data):

        if index > 0:
            data_line = line.strip()

            columns = data_line.split(',')

            entity.append(columns[0])
            entity_code.append(columns[1])
            year.append(columns[2])
            life_expectancy.append(columns[3])

min_value = min(life_expectancy)
max_value = max(life_expectancy)

min_value_country = entity[life_expectancy.index(min_value)]
max_value_country = entity[life_expectancy.index(max_value)]

print(f'The lowest value for life expectancy is {min_value} in {min_value_country}')
print(f'The highest value for life expectancy is {max_value} in {max_value_country}')

country_input = input('Enter the country that your are interested: ')
year_input = input('Enter the year of interest: ')

values_for_selected_country = []

for index, e in enumerate(entity):
    if e.lower() == country_input.lower():
        values_for_selected_country.append(life_expectancy[index])

if len(values_for_selected_country) > 0:
    print(f'The lowest value for life expectancy is {min(values_for_selected_country)} in {country_input}')
    print(f'The highest value for life expectancy is {max(values_for_selected_country)} in {country_input}')
else:
    print(f'There is not any result for country {country_input}')
