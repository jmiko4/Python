'''Author Justin Mikolajcik
Lets do some neat-o code'''

first= input('What is your first name?: ')
last = input('What is your last name: ')
email = input('What is your email adress: ')
phone = input('What is your phone number: ')
job = input('What is your job title: ')
id = input('What is your ID number: ')
hair = input('What is your hair color: ')
eyes = input('What color are your eyes: ')
month = input('What month did you start in: ')
training = None 
while training not in ("yes", "no"): 
    training = input("Do you have training: ") 
    if training == "yes": training = ('yes')
        
    elif training == "no": training = ('no')
         # Do that. 
    else: 
    	print("Please enter yes or no.")

#sorry for long code, ill probably not do that next time
print(f'----------------------------------------\n[{last.upper()}], [{first}]\n[{job.capitalize()}]\nID: [{id}]\n\n[{email.lower()}]\n[{phone}]')
print(f'\nHair: {hair:15} Eyes: {eyes}')
print(f'Month: {month:15}Training: {training}')
print('----------------------------------------')
