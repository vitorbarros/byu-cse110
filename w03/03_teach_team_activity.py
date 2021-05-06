import math

# functions definition
def square_area_calc(length):
    return str(float(length) * 2)


def rectangle_area_calc(length, width):
    return str((float(length) * float(width)) / 2)


def circle_area_calc(radius):
    return str(math.pi * (float(radius) ** 2))


# square area
square_length = input('What is the length of a side of the square? ')
print(f'The area of the square is: {square_area_calc(square_length)}')

# rectangle area
rectangle_length = input('What is the length of rectangle? ')
rectangle_width = input('What is the width of rectangle? ')
print(f'The area of the rectangle is: {rectangle_area_calc(rectangle_length, rectangle_width)}')

# circle radius
circle_radius = input('What is the radius of the circle? ')
print(f'The area of the circle is: {circle_area_calc(circle_radius)}')
