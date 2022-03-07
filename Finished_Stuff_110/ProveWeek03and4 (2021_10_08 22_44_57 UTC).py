'''Author JUSTIN MIKOLAJCIK
    LETS FEED ADULTS AND CHILDREN AND DO MATH
    SAMPLE TEXT'''

childprice = float(input('Welcome to Wendys\nHow much does the child\'s meal cost?\n'))
adultprice= float(input('And how much does the adult\'s meal cost?\n'))
drinkcost = float(input('How much do the drinks cost?\n'))
#Now we are feeding
child = int(input('How many children are we feeding?\n'))
adult = int(input('How many adults are we feeding?\n'))
drinks = int(input('How many drinks do we need?\n'))
#lets find tax
tax = float(input('What is the sales tax rate?\n'))
#do some math now and print the answers
b4tax=((childprice*child)+(adult*adultprice)+(drinkcost*drinks))
answer = float(round(b4tax, 2))
print(f'The subtotal is ${answer}')
aftertax = ((tax/100)*b4tax)+b4tax
answer2 = str(round(aftertax, 2))
print(f'After tax the price is ${answer2}')
#Now lets find their change
money = float(input('What is the payment amount? $'))
change = float(money - aftertax)
print (f'${change:.2f}')
