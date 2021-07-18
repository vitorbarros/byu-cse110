def wind_chill(temperature, wind_speed):
    return 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)


def convert_to_fahrenheit(value):
    return value * (9 / 5) + 32


def wind_speed_loop():
    return


temp_input = int(input('What is the temperature? '))
unit_input = input('Fahrenheit or Celsius (F/C)? ')

temp = 0
times = 12

for t in range(12):
    step = (t + 1) * 5
    if unit_input.lower() == 'c':
        temp = convert_to_fahrenheit(temp_input)
    else:
        temp = temp_input

    wind = wind_chill(temp, step)

    print(f'At temperature {temp:.2f}F, and wind speed {step} mph, the windchill is: {wind:.2f}F')
