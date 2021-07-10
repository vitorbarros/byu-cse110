friends_list = []

friend = ''

while friend != 'end':
    friend = input('Type the name of a friend: ')
    if friend != 'end':
        friends_list.append(friend)

print()
print('Your friends are:')

for friend in friends_list:
    print(friend)
