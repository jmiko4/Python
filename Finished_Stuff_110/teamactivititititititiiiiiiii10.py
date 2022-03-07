'''Welcome to justins fun emporium
I need a nap
and maybe some xanax
'''

bank_accounts = []
balances = []
count=0
total = 0
again = 'yes'
ans = None

while ans != 'quit':
    ans = input('Alright you lemon, give me a bank account thing i guess or type quit to stop\n')
    
    if ans != 'quit':
        bank_accounts.append(ans)
        balances.append(float(input('Alright you monster give me the account value\n')))

    count+=1

print('Account information:')

for i in range(len(bank_accounts)):
    print(f'{i+1}. {bank_accounts[i]} - {balances[i]}')
    total += balances[i]

max_val = max(balances)
print(f'Total: {total}')
print(f'Average {total/len(balances):.2f}')
print(f'Highest account:{bank_accounts[balances.index(max_val)]} {max(balances)}')

while again == 'yes':
    again = input('Would you like to update an account?')
    if again == 'yes':
        update =(int(input('Which account would you like to update'))-1)
        new_amount = float(input('What is the new amount'))
        balances[update] = new_amount
    for i in range(len(bank_accounts)):
        print(f'{i+1}. {bank_accounts[i]} - {balances[i]}')
        total += balances[i]
        





    
