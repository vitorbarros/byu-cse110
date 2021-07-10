def menu():
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    return int(input('Please enter an action: '))


def add_item():
    item = input('What item would you like to add? ')
    price = float(input(f'What is the price of "{item}"? '))

    print(f'{item} has been added to the cart.')

    return [item, price]


def view_cart(items_list, price_list):
    for index, item in enumerate(items_list):
        i = index + 1
        print(f'{i}. {item} - ${price_list[index]:.2f}')


def remove_item(items_list, price_list):
    index = int(input('Which item would you like to remove? '))
    items_list.pop(index - 1)
    price_list.pop(index - 1)

    return [items_list, price_list]


def total(price_list):
    print(f'The total price of the items in the shopping cart is ${sum(price_list):.2f}')


print('Welcome to the Shopping Cart Program!')

menu_item = menu()
cart_items = []
items_price = []

while menu_item != 5:
    if menu_item == 1:
        response = add_item()
        cart_items.append(response[0])
        items_price.append(response[1])
        menu_item = menu()
    if menu_item == 2:
        view_cart(cart_items, items_price)
        menu_item = menu()
    if menu_item == 3:
        response = remove_item(cart_items, items_price)
        cart_items = response[0]
        items_price = response[1]
        menu_item = menu()
    if menu_item == 4:
        total(items_price)
        menu_item = menu()

if menu_item == 5:
    print('Thank you. Goodbye.')
