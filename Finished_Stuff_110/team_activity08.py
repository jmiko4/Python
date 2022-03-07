num = range(int(input('How many rows and collumns would you like?\n')))
for col in num:
     for row in num:
        print(f'{(row+1)*(col+1):3}', end='  ')
     print()