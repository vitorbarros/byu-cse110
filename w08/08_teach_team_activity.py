import math

columns_and_rows = int(
    input('How many columns and rows do you want in your multiplication table? '))

columns = range(1, columns_and_rows + 1)
rows = range(1, columns_and_rows + 1)

digits = int(math.log10(columns_and_rows)) + 1

for column in columns:
    r = ''
    for row in rows:
        r += f'{row * column:{digits * 3}}'
    print(r)
