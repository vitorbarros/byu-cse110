def subtotal_calc(c_price, a_price, t_childrem, t_adults):
    return (c_price * t_childrem) + (a_price * t_adults)

def sales_tax_calc(subtotal, tax):
    return (subtotal * tax) / 100


childs_price = float(input('What is the price of a child\'s meal? '))
adults_price = float(input('What is the price of an adult\'s meal? '))
total_of_children = int(input('How many children are there? '))
total_of_adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))

subtotal = subtotal_calc(childs_price, adults_price, total_of_children, total_of_adults)
sales_tax = sales_tax_calc(subtotal, tax_rate)

print(f'\nSubtotal: ${subtotal}')
print(f'Sales Tax: ${sales_tax}')