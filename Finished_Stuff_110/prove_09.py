'''So this program was made by only looking at the first few lines of the prove activity instructions. 
This is basically what my brain said to do when i looked at the promt
also i have a ton of count variables but thats ok'''
'''Un programa escrito por : Tu mamá por las dudas'''
import time

print('Hi welcome to Amazon, Lets do some shopping')


#So I like java because we declare all of out variables at the beginning.
items = []
prices = []
count = 0
count1 = 0
count2 = 0
count4 = 1
cart_total = 0
remove=None
choice = 0


while choice != 5:
    choice = int(input('\nWhat would you like to do?\n1. Add an item\n2. View shopping cart \n3. Remove from the cart\n4. View the subtotal\n5. End program\n'))
    time.sleep(.5)
    if choice == 1:
        items.append(input('What is the item name?\n'))
        prices.append(float(input('What is the price?\n')))
        # wow = items[count]
        print(f'{items[count]} has been added to the cart')
        # print(wow)
        count +=1

    elif choice == 2: 
        print('Here is your cart')
        for n in items:
            print(f'{n} is {prices[count1]}')
            
            count1+=1
    
    elif choice == 3:
        print('Which of these items would you like to remove?')
        for i in range(len(items)):
            print(f'{i+1}. {items[i]}')
        remove = (int(input())-1)
        print(f'{items[remove]} has been removed')
        items.remove(items[remove])
        prices.pop(remove)
        count1 =-1

    elif choice == 4:
        for i in range(len(prices)):
            cart_total+=prices[i]
        print(f'Your subtotal is {cart_total}')    
    
    elif choice !=5 :
        choice = 0
    time.sleep(.75)
