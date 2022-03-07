'''Bing bong bing bong
Author:Yours truly.
Bing bing bong
So the purpose of this activity is to ensure that no one dies on the rolla costa
'''
print('WELCOME TO SIX FLAGS DISCOVERY KINGDOM.\nYOU ARE ABOUT TO GET ON THE RIDE OF DEATH, THE ROLLER COASTER WITH THE HIGHEST CHANCE OF DEATH IN THE STATE OF IDAHO')
age1=int(input('How old are you (in years pls)?\n'))
height1 = int(input('HEY HOW TALL ARE YOU in inches por favor?\n'))
passport = input('Does the rider have a golden passport?(yes/no)')
#UWU
#OH NOW LETS DO SOME IF STATESMETNSSEsa
#I WANT TO REWATCH THE STAR TREK REMAKE FROM LIKE 2015
if height1 <36:
    can_ride=False
elif height1 >=62 and age1>=18:
    can_ride=True
elif age1>=12 and age1<=17 and passport=='yes':
    can_ride=True
else:
    second_rider=input('Is there anotha human person?????????????(yes/no)\n').lower()
    if second_rider == 'yes':

        age2=int(input('HEY WHAY IS THE AGE OF THE SECOND HUMAN PERSON IN years PLEASE\n'))
        height2= int(input('What is the second rider\'s height?\n'))

        if (age2 >= 18 or age1 >= 18) and height2 >=36 :
            can_ride=True
        elif age1>=12 and height1>=52 and age2>=12 and height2>=52:
            can_ride=True
        elif (age1>=12 and age1<=17) or (age2>=12 and age2<=17):
            passport2=input('Does the second rider have a GOLDEN PASSPORT?(yes/no)\n')
            if passport2 == 'yes' or passport == 'yes':
                can_ride=True
        
        else:
         can_ride=False
    else:
        can_ride=False

if can_ride:
    print('CONGRATULATIONS YOU MAY RIDE')
else:
    print('GROW UP AND YOU MIGHT RIDE LATER ON IN LIFE')




