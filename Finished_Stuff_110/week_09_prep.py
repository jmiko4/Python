
names = []
name = ''

while name != 'end':
    name = input('Type the name of a friend: ')
    if name != 'end':
        names.append(name)


for n in names:
    print(n)
