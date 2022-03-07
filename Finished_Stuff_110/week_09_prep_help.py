ans=None
items=[]
while ans != 'quit':
    ans = input('What is the item name?\n')
    if ans!= 'quit':

     items.append(ans)

print ('The shopping list is:')
for i in items:
    print(i)
    
print('The shopping list with indexes is: ')

for i in range(len(items)):
    print(f'{i+1}. {items[i]}')

change = int(input('Which item would you liek to chagbne01'))

items.pop(change-1)

new_item =input('What is the new itme')
items.insert(change-1,new_item)

for i in items:
    print(i)
