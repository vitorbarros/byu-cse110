def subtotal_calc(c_price, a_price, t_childrem, t_adults):
    return (c_price * t_childrem) + (a_price * t_adults)


def sales_tax_calc(subtotal, tax):
    return (subtotal * tax) / 100


def total_calc(subtotal, sales_tax):
    return subtotal + sales_tax


def change_calc(payment_amout, total):
    return payment_amout - total


def request_payment_amout():
    return float(input('\nWhat is the payment amount? '))


childs_price = float(input('What is the price of a child\'s meal? '))
adults_price = float(input('What is the price of an adult\'s meal? '))
total_of_children = int(input('How many children are there? '))
total_of_adults = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))

subtotal = subtotal_calc(childs_price, adults_price,
                         total_of_children, total_of_adults)

sales_tax = sales_tax_calc(subtotal, tax_rate)
total = total_calc(subtotal, sales_tax)

print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

payment_amout = request_payment_amout()

if (payment_amout < total):
    print('\nthe payment amount cannot be less than the total, please provide a valid value')
    payment_amout = request_payment_amout()


change = change_calc(payment_amout, total)

print(f'Change: ${change:.2f}')
