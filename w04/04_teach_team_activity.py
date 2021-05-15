import math

print('Welcome to velocity calculator. Please enter the following:')
m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s**2, 9.8 for Earth, 24 for Jupiter):'))
t = float(input('Time (in seconds):'))
p = float(input('Density of fluid (in kg/m**3, 1.3 for air, 1000 for water):'))
a = float(input('Cross sectional area (in m**2):'))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder):'))

c = (1 / 2) * p * a * C
v = math.sqrt(m*g/c)
velocity = (1 - math.exp(v/m)*t)
velocity_time = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))

print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after {t} seconds is: {velocity_time:.3f} m/s')
