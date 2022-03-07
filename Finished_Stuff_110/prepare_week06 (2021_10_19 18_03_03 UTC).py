'''Neat program stuff
Author:Yours truly
lets loan some money'''
lsize = int(input('On a scale of 1-10 how large is the loan?'))
credit = int(input('On a scale of 1-10 how good is your credit history?'))
income = int(input('On a scale of 1-10 how high is your income?'))
down_payment  = int(input('On a scale of 1-10 how large is your down payment?'))
is_qualified=False

if lsize >=5:
    if credit >=7 and income>=7:
        
        is_qualified=True
    elif (credit>=7 or income>=7) and down_payment >= 5:
        is_qualified=True    
elif credit< 4:
    is_qualified=False
elif income>=7 or down_payment >=7:
    is_qualified=True
elif income>=4 and down_payment>=4:
    is_qualified=True
else:
    is_qualified=False

if is_qualified:
    print('Congratulations! You have qualified for the loan')
else:
    print('Were sorry but you do not qualify')